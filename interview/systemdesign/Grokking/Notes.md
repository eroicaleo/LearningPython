
# Unit 1: System Design Interviews: A step by step guide

## Step 1: Requirement clarifications

* Ask questions:
    * exact scope of the problem
    * what parts of the system we will be focusing on

* Use Twitter as an example
    * Will users be able to post tweets and follow other people?
    * create and display the user's timeline?
    * Tweets contain photos and videos?
    * Backend only or front-end too?
    * Search Tweets?
    * Display hot trending topics?
    * Need push notification?

## Step 2: Back-of-the-envelope estimation

* Estimate scale of the system, decide to do scaling, partition, load balancing and caching.
    * What scale is expected from the system: no of new tweets/views/timeline generation per sec.
    * How much storage? If need to have photos/videos then different.
    * network bw usage are we expecting? Determine traffic and balance load between servers.

## Step 3: System interface definition

* Establish the exact contract expected from the system
* Make sure we haven't gotten any requirements wrong

```python
postTweet(user_id, tweet_data, tweet_location, user_location, timestamp, ...)
generateTimeline(user_id, current_time, user_location, ...)
markTweetFavorite(user_id, tweet_id, timestamp, ...)
```

## Step 4: Defining data model

* Defining Data model:
    * Early stage: clarify how data will flow between different components of the system.
    * Later: guide for data partition and management
* Identify various entities of the system, how they will interact with each other.
* Different aspects of data management:
    * Storage
    * transportation
    * encryption
* The entities for Twitter-like service:

```python
User: UserID, Name, Email, DoB, CreationData, LastLogin
Tweet: TweetID, Content, TweetLocation, NoOfLikes, TimeStamp
UserFollowo: UserdID1, UserID2
FavoriteTweets: UserID, TweetID, TimeStamp
```

* Additional questions:
    * Which DB should we use?
    * NoSQL like Cassandra, or MySQL?
    * What kind of block storage should we use to store Photos and videos?

## Step 5: High-level design

* Draw 5-6 boxes representing the core components of our system
    * Identify enough components
* Twitter:
    * Multiple application servers to serve all the read/write requests
    * Load balancers in front of them for traffic distribution
    * More read than write, then have separate servers for handling these scenarios.
    * An efficient DB that can store all tweets and can support a huge number of reads.
    * A distributed file storage system for photos and videos.

## Step 6: Detailed design

* Dig deeper into 2 or 3 major components. Interviewer will guide us.
* We present different approaches, their pros and cons
* No single anwsers, tradeoff is more important

* We will be storing massive amount of data, how should we partition our data?
    * How do we distribute it to multiple DBs?
    * all the data of a user on the same DB?
    * What issue could it cause?
* How to handle hot users who tweet a lot or follow lots of people?
* Timeline will contain the most recent and relevant tweets, should we store our data
  in such a way that is optimized for scanning the latest tweets?
* How much and at which layer should we introduce cache to speed things up?
* What components need better load balacing?

## Step 7: Identifying and resolving bottlenecks

* Try to discuss as many bottlenecks as possible and different approaches to mitigate them
    * single point of failure?
    * enough replicas of data?
    * enough copies of different services?
    * How are we monitoring the performance? Do we get alert when critical components failed?

## Step 8: Conclusion

* Preparation and being organized

# Unit 2: Designing TinyURL

* similar service: bit.ly, goo.gl, qlink.me

## Why do we need URL shortening?

* Save space when messaging/tweeting

## 2.2 Requirements and Goals of the System

* exact scope of the problem
* what parts of the system we will be focusing on

* Functional Requirements:
    * URL -> our service should generate a shorter and unique alias of it. Should be short enough.
    * Users access the short link, our service should redirect them to the original link.
    * Users can pick a custom short link for their URL.
    * Links will expire after certain time. Users can also specify the expiration time.
* Non-Functional Requirements:
    * Should be highly available, if not, redirection is impossible
    * Redirection should be min latency
    * Shortened links should be unpredictable
* Extended Requirements
    * Analytics, how many times a redirection happened?
    * Our service should be accessible through REST APIs by other services

## 2.3 Capacity Estimation and Constraints (Back-of-the-envelope)

* Read heavy, assume 100:1 read:write
* Traffic estimates
    * Assume 500M shortening per month, read is 50B
    * QPS: 200 URLs and 20K/s read
* Storage estimates
    * Keep the URL for 5 years
    * 500M * 5Yr * 12 Mon = 30B
    * Each stored object will be 500B, then it's 15TB
* Bandwidth estimates
    * Writes: 200 * 500B = 100 KB/s
    * Reads: 20K * 500B = 10 MB/s
* Memory
    * Follow 80-20 rules, cache 20% hot URLs
    * Reads: 20K/s * 3600 * 24 = ~1.7B
    * To cache 20% of these requests, 0.2 * 1.7 billion * 500B = ~170GB

* New URLs : 200/s
* URL redirection : 20K/s
* Incoming data : 100KB/s
* Outgoing data : 10MB/s
* Storage for 5 yr : 15TB
* Memory for cache : 170GB

## 2.4 System APIs (System interface definition)

* Once Requirements has been finalized, good idea to define the system APIs
  Explicitly state what is expected from the system.

```python
createURL(api_dev_key, original_url, custom_alias=None, user_name=None, expire_data=None)
```

* Parameters:
    * `api_dev_key` : API developer key of a registered account, throttle users based on their allocated quota
    * `original_url` : Original URL
    * `custom_alias` : Optional custom key for the URL
    * `user_name` : Optional user name to be used in encoding
    * `expire_data` : Optional expiration date for the shortened URL

* Returns:
    * Success, the shortened URL
    * Failure, error code

```python
deleteURL(api_dev_key, url_key)
```

* `url_key` :  a string representing the shortened URL
* Returns: URL removed

* Prevent abuse: `api_dev_key` can be limited to a certain number of URL creation and redirection for some period.

## 2.5 DB Design (Defining data model)

* Defining the DB schema in early stages can help understand the data flow among various components
  and later would guide towards data partition

* Observations about the nature of the data:
    * billions of records
    * Each object is small
    * No relationship between records - other than storing which user created a URL
    * Service is read-heavy

* DB Schema:
    * Table 1: URL mappings
        * Hash: varchar(16)
        * OriginalURL: varchar(512)
        * Creation/Expiration Date: datetime
        * UserID: int
    * Table 2: User's data
        * UserID: int
        * Hash: varchar(20)
        * email: varchar(32)
        * Creation/LastLogin Date: datetime

* NoSQL or SQL?
    1. billions of rows, i.e. large amount of data
    2. no relationships between objects
    3. NoSQL is the choice

## 2.6 Basic System Design and Algorithm (High-level design)

* problem: generate a short and unique key for a given URL

### 2.6.1 Encoding actual URL

* Compute unique hash of the given URL: base36/base62/base64
* What should be the length of the short key? 6, 8, 10?
    * 64^6 ~ 68.8B (Assume it's enough)
    * 64^8 ~ 281T
* MD5 algorithm produce 128-b hash value, after base64 encoding, it's 22 chars
  Then we take the first 6/8 letters.
    * swap some characters

#### Issues

* Multiple users enter the same URL, get the same shortened URL
* Parts of the URL are URL encoded: `?=%3F, ==%3D`

```
www.educative.io/distributed.php?id=design
www.educative.io/distributed.php%3Fid%3Ddesign
```

* Workaround
    1. append increasing sequence no. Why we don't need store this sequence number?
       Can the number overflow? Also impact the performance of the service.
    2. append the user id. What if the user hasn't signed in? We need to ask the user
       to choose a unique key. But if we have a conflict, we have to ask the user
       to choose another one, until it's unique

### 2.6.2 Request flow for shortening of a URL

1. Client sends the URL to short, Server receives the URL
2. Server encode the URL, i.e. `?=%3F, ==%3D` etc, sends it to encoding service
3. encoding service sends the encoded URL to DB
4. DB found the encoded URL has stored, return "failed due to duplication" to server
5. server appends sequence or userid to the original sequence and sends it again to encoding service
6. repeat 3
7. DB found the encoded URL is a new entry, return "successfully inserted" to server
8. Server return shortened URL to client

### 2.6.3 Generating keys offline

* Key Generation Service (KGS) generates random six-letter before hand
  and stores them in a DB.
* Whenever needed, just take one from DB
* Simple and fast: no encoding/duplications/collisions

#### Issues

* Concurrency: multiple servers reading keys at the same time
* Solution: KGS one table for not used keys, another for used keys
    1. Load some keys into memory
    2. move them immediately to used keys table, even before assigning them to any server
    3. if KGS dies, we lost some keys, but not a problem
    4. KGS needs to make sure not giving same key to multiple servers:
       get a lock before removing key

* key-DB size: 6 chars X 68.7B keys X 1 B/char = 412 GB.
* KGS a single point failure?
    * Yes, have a standby replica of KGS. Primary dies, standby one to generate and provide keys
* Can each app server cache some keys?
    * Yes. Speed things up, but we might end up losing those keys.
* How to perform a key loopup?
    * Lookup the key in DB to get full URL
    * found, then issue "HTTP 302 Redirect"
    * Not found, "404"
* Should we impose size limits on custom aliases?
    * Users can pick a custom alias, better to limit the size, so we can have
      a consistent URL DB.

### 2.6.4 High level design for URL shortening

client <------------>  application server <------------ KGS
                        ^                                ^
                        |                                |
                        |                                |
                        |                                |
                        V                                V
                        DB                               key-DB

## 2.7 Data Partition and Replication (Detailed design)

* Need to partition the data to store billions of URL
* Divide and store data into different DB servers

### 2.7.1 Range Based Partition

* The location based on the first letter of key, 'A' -> server 1, 'B' -> server 2
* Can consolidate less frequent letters into one server.
* drawbacks: Unbalanced DB

### 2.7.2 Hash Based

* Compute the hash value of the key, it's between [0,255].
* Consistent hashing will help to mitigate the overloaded problem.

## 2.8 Cache (Detailed Design)

* Cache URLs that are frequently accessed. like Memcached
* Application server checks cache first before hitting DB
* How much memory we need?
    * 20% of daily traffic, i.e. 170G from previous calculation, easy to fit in one server
    * Alternatively, use a couple of smaller servers to store all hot URLs
* Which cache eviction policy would best fit?
    * Least Recently Used (LRU)
    * Use "Linked Hash Map" to implement LRU
* How can each cache replica be updated?

### 2.8.1 Request flow for accessing a shortened URL (with cache)

1. Client access a shortened URL to application server
2. server tries to find original URL in cache
3. URL found in Cache
4. check URL expired or user doesn't have permission?
5. Return 401 / Or redirect to original URL
6. URL not found in Cache
7. application try to find original URL in DB.
8. URL does not find in DB
9. go to step 5
10. URL found in DB, update Cache, then go to step 3.

## 2.9 Load Balancer (LB) (Detailed Design)

* Three places can have load balancer
    * Between clients and application servers
    * Between application servers and DB servers
    * Between application servers and Cache servers

* Round Robin (LB)
    * simple to implement, no overhead
    * when a server is dead, will just skip it
    * However, we don't take server load into consideration, need to use more intelligent LB solution

## 2.10 Purging or DB cleanup

* Link expired? How to remove them?
* Active search
    * A lot of more pressure on our DB.
* Lazy cleanup
    * User tries to access an expired link, we can delete the link
    * Seperate Cleanup service can run periodically from storage and cache
      must be lightweight and run only when user traffic is to be low
    * Default expiration time for each link
    * After removing, the key can be put in the key-DB for reusing
    * Should we remove links not visited in some length of time
      storage is cheap, keep links!

## 2.11 Telemetry

* country of the visitors
* date and time of access, web page that refers the click
* browser
* platform from where the page was accessed?

## 2.12 Security and Permissions

* Private URLs or a set of users to access URL?
* One additional column to store the UserIDs who have the permission.

# Unit 3: Designing Pastebin

Users store plain text and get a randomly generated URL to access it.
pastebin.com, controlc.com, hastebin.com

## 3.1 What is Pastebin?

* Store plain text or images

## 3.2 Requirements and Goals of the System

* Functional Requirements
1. Users should be able to upload or "paste" their data and get a unique
   URL to access it.
2. Only text allowed.
3. Data and links will expire after a specific timespan.
   Users should also be able to specify expiration time.
4. Users can pick a custom alias for their paste.

* Non-Functional Requirements
1. Highly reliable, data uploaded should not be lost
2. Highly available, the service cannot be down
3. Access their Pastes in real-time with min latency.
4. Paste links should not be guessable (not predictable)

* Extended Requirements:
1. Analytics, how many times a paste was accessed?
2. Our service should be accessible through REST APIs by other services.

## 3.3 Some Design Considerations

* Share some requirements with URL shortening service.
  There are some additional design considerations.
* The limit on amount of text each time: 10MB.
* Impose a size limit on custom URLs.

## 3.4 Capacity Estimation and Constraints (Back-of-the-envelope)

* Read heavy, 5:1 read : write
* Traffic estimates
    * Not so heavy
    * 1M new paste everyday, 5M read / day
    * 1M / (24hr * 3600) ~= 12 pastes / sec, 58 reads/sec
* Storage estimates:
    * Avg 10KB/pastes, so 10 GB/day
    * Store 10 yr, total capacity is 36TB
    * how many keys? Since 1M pastes/day, then 3.6B pastes in 10yr.
    * base64 encoding, 6 letters, then we can have 68.7B unique strings.
    * 3.6B * 6 ~ 22G << 36TB
    * Assume we can only use 70% capacity, we need 51.4 TB.
* Bandwidth estimates
    * 12 pastes/sec * 10KB = 120 KB/s
    * 58 read/sec * 10KB ~ 0.6 MB/s
    * Not big but keep them in mind
* Memory estimates
    * Still cache 20%
    * 5M read/day * 10KB * 20% ~= 10 GB

## 3.5 System APIs (System interface definition)

```python
addPaste(api_dev_key, paste_data, custom_url=None, user_name=None, paste_name=None, expire_data=None)
```

* Parameters:
    * `api_dev_key` : API developer key of a registered account, throttle users based on their allocated quota
    * `paste_data` : string 
    * `custom_url` : string, Optional custom key for the URL
    * `user_name` : Optional user name to be used in generate URL
    * `paste_name` : string, optional name of the paste
    * `expire_data` : Optional expiration date for the shortened URL

* Returns:
    * Success, the URL we can access the paste
    * Failure, error code

```python
getPaste(api_dev_key, api_paste_key)
deletePaste(api_dev_key, api_paste_key)
```

## 3.6 DB Design (Defining data model)

* Observations about the nature of the data:
    * billions of records
    * Each metadata object is small
    * Each paste object can be medium size (up to 10 MB)
    * No relationship between records - other than storing which user created what paste
    * Service is read-heavy

* DB Schema:
    * Table 1: Paste
        * URLHash: varchar(16)
        * ContentKey: varchar(512), a reference object storing the contents of the paste
        * Creation/Expiration Date: datetime
        * UserID: int
    * Table 2: User's data
        * UserID: int
        * Hash: varchar(20)
        * email: varchar(32)
        * Creation/LastLogin Date: datetime

## 3.7 High Level Design

client <------------>  application server <------------ Object storage
                        ^
                        |
                        |
                        |
                        V
                        Metadata Storage

* Separate storage layer
* One DB to store metadata related to each paste
* One DB to store paste contents

## 3.8 Component Design

### 3.8.1 Application layer

#### How to handle a write-request?

1. Receiving a write-request, generate a 6-letter random string, it's the key.
2. Store the contents, store the generated in DB.
3. Return the key to user.
4. In case random key exists, keep generating until not duplicating.
   Also return error to user, if custom key already present in DB.

* Another approach: Key Generation Service (KGS)
  Exactly same as the shortened link.

* KGS: single point failure? Yes, but we can have a replica of KGS and
  whenever the primary server dies.

* Each application server can cache some keys from key-DB. Lose the keys
  when application server.

* Handle read request
    * application service contacts the DB.
    * DB searches for the key, if key is found, returns the paste's contents.
    * Otherwise, return error code.

### 3.8.2 DB layer

Two layers:

1. Metadata DB: relational DB like MySQL or Distributed Key-value store like Dynamo or Cassandra.
2. Object storage: Object storage like Amazon S3. Whenever hitting the full capacity on  
   content storage, increasing by adding more servers.

The flowchart: skip for now.

## 3.9 Purging or DB cleanup
## 3.10 Data Partitioning and Replication
## 3.11 Cache and Load Balancer
## 3.12 Security and Permissions

* See the first lecture.

#  Unit 4: Designing Instagram

* Photo sharing service, users can upload photos to share them with other users.

## 4.1 What's Instagram?

* Social App.
* User can choose to share publicly or privately.
* Allow users to share through other social app, FB, Twitter, etc.
* We design Simpler version, user can share and follow.
* Newsfeed for all top photos.

## 4.2 Requirements and Goals of the System

* Functional Requirements
1. users upload/download/view photos
2. U search based on photo/video titles
3. U follow other users.
4. generates and display user's Newsfeed: top photos from all the people the user follows.

* Non-functional Requirements
1. Highly available.
2. News Feed generation: 200ms
3. Consistency can take a hit, U doesn't see a photo, it's fine.
4. Highly reliable, photo and video should never be lost.

* Out of scope Requirement
    * Adding tags/searching based on tags/commenting on photos, tagging users to photos.

## 4.3 Some Design Considerations

* Read heavy. Our focus should be building a system that can retrieve photos quickly.
* Pratically, users can upload as many photos. Need to efficient management of storage.
* Low latency for viewing photos.
* 100% reliable. Photos should not be lost.

## 4.4 Capacity and Constraints

* Assume 500M Total users, 1M daily active users
* 2M new photos every day, 2M/(24 * 3600) = 23 new photos every second
* Average photo size ~ 200KB
* Disk space for 1 day new photos: 2M * 200 KB ~ 400 GB
* Total space for 10 yr ~= 1425 TB

## 4.5 High level System Design

* Two scenarios:
    1. upload photos.
    2. view/search photos.
* Object storage servers to store photos.
* Some DB servers to store metadata info about photos.

User upload image----------------> |------------------------|-----------> image storage
                                   |                        |
                                   | image hosting system   |
                                   |                        |
User view/search image-----------> |------------------------|-----------> image metadata

## 4.6 DB Schema

* Store data:
    * about users
    * their uploaded photos
    * people they follow

* Table 1: photo table

| PK | PhotoID: int        |
|----|---------------------|
|    | UserID: int         |
|    | PhotoLatitude: int  |
|    | PhotoLongitude: int |
|    | UserLatitude: int   |
|    | UserLongitude: int  |
|    | CreationDate: datetime  |

* Table 2: User table

| PK | UserID: int             |
|----|-------------------------|
|    | Name: varchar(20)       |
|    | Email: varchar(32)      |
|    | DateOfBirth: datetime   |
|    | CreationDate: datetime  |
|    | LastLogin: datetime     |

* Table 3: UserFollow

| PK | UserID1: int |
|    | UserID2: int |
|----|--------------|

* Relational DB is not easy to scale, see SQL vs. NoSQL
* Photos will be stored in distributed file storage like HDFS or S3
* Store all 3 tables in a distributed key-value store
* how to store relationship between users and photos? how to store follow relations?
    * wide-column like Cassandra
    * a list of PhotoIDs, a list of following Users
* Other benefits of Cassandra:
    * automatically maintain certain number of replicas.
    * data is retained for certain days (to support undeleting).

## 4.7 Data Size Estimation

# Q&A

Q: In 2.6.1, Why we don't need store this sequence number?
A: Is it because in the 2.6.2 diagram, it will keep looping steps 3 ~ 6, until the encoded URL is new.

Q: In 2.6.3, single point failure. How the standby take over?
A: Assume the not used keys and the used keys are stored in disk, and the disk doesn't die.
   Then it makes sense. Otherwise, if the disk also died, seems not be able to recover

Q: In 2.7, it doesn't actually cover data replication.
