
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

* User table entry: ID(4B) + Name(20B)+Email(32B)+3xdates(12B) = 68B
    * 500M Users * 68B = 32G
* Photo table entry is similar: 284B
    * 2M new photos / day, 2M * 284B ~= 0.5GB/day
    * 10 years ~ 1.88T
* UserFollow table:
    * Every one follow 500 followers * 5M users * 8 bytes ~= 1.82 TB
* Total space in 10 yr ~ 3.7 TB

## 4.8 Component Design

* Uploads can be slow, it goes to disk. Reads will be fast, if we have cache.
* Webserver has certain connection limit, and also write is slow.
  So we need to use different servers for reads and writes service.
* Seperation will also allow us to scale and optimize independently.

User upload image----------------> |------------------------|-----------> image storage
                                   | image upload service   |   ^
                                   |                        |   |
                                   |------------------------|------|
                                                                |  |
                                                                |  |
                                   |------------------------|---|  |
                                   | image download service |      V
                                   |                        |      V
User view/search image-----------> |------------------------|-----------> image metadata

## 4.9 Reliability and Redundancy

* Losing files is not an option. We will store multiple copies of each file.
* Same principle also applies to other components of the system. Have multiple replicas.
* Run a redundant secondary copy of the service that is not serving any traffic. Take control when primary has a problem.
* Redundancy can remove single points of failure.

User upload image----------------> |------------------------|-----------> image storage/replica 1/replica 2
                                   | image upload service   |   ^
                                   | 1, 2, 3                |   |
                                   |------------------------|------|
                                                                |  |
                                                                |  |
                                   |------------------------|---|  |
                                   | image download service |      V
                                   | 1, 2, 3                |      V
User view/search image-----------> |------------------------|-----------> image metadata/backup 1

## 4.10 Data Sharding

### 4.10.1 Partition based on UserID

* we can keep all photos of a user on the same shard. Assume we have 10 shards.
* Find shard number by UserID % 10, store the data. We can append shard number with each PhotoID.
* Each DB shard can have its own auto-increment sequence for PhotoIDs. And we will append
  ShardID with each PhotoID, so they are unique.

#### 4.10.1.1 Issues with this partitioning scheme.

1. How to handle hot users? A lot of other people see photos uploaded by the hot users.
2. Some users have a lot of more photos compared to others, non-uniform distribution of storage.
3. What if we have to store all pictures of a user onto multiple shards?
4. Store all photos of a user on one shard, if the shard is down, or higher latency if load is high.

### 4.10.2 Partition based on PhotoID

* If we can generate unique photoIDs first and then find a shard number: `PhotoID%10`.
* How to generate PhotoIDs?
    * Dedicate a seperate DB instance to generate auto-incrementing IDs.
    * PhotoID should be able to fit into 64-bit number, 2^64 ~ 10^18.
    * We define a table containing only a 64-bit field.
* The above one is a single point of failure.
* Workaround 1:
    * Two servers, one to generate even numbered ID, one to generate odd numbered ID.
    * Load balancer: round robin between them
    * We can even extend to generate separate ID tables for Users, Photo-Comments, or
      other objects.

```
KeyGeneratingServer1:
auto-increment-increment = 2
auto-increment-increment = 1

KeyGeneratingServer2:
auto-increment-increment = 2
auto-increment-increment = 2
```

* Workaround 2:
    * Use key generation scheme similar to URL shortening service.

### 4.10.3 Future growth of our system

* We can have logical partition at the begining.
* These partitions can sit in one server at the begining.
* When one partition is getting a lot of data, we can migrate
  some logical partitions from it to another server.
* Have a config file or DB to track the mapping between logical partitions
  and DB servers.

## 4.11 Ranking and News Feed Generation

* Assume fetching top 100 photos.
* Get the list of people the user follow.
* Get the meta data of 100 photos from each user.
* Submit all these photos to ranking algorithm which will determine top 100 photos
  (based on recency, likeness)
* Problem with this approach: higher latency, because we have to query multiple tables
  and perform sorting/merging/ranking on the results.
* To improve efficiency, pre-generate the News Feed and store it.

### 4.11.1 Pre-generating the News Feed

* Dedicated servers that are continuously generating users' News Feeds and storing
  them in a 'UserNewsFeed' table
* We will just query this table
* Whenever these servers need to generate the News Feed, first query the UserNewsFeed
  table to find the last time generated. Then new UserNewsFeed data will be generated from that time.

### 4.11.2 Different approaches for sending News Feed contents to users.

* Pull
    * Clients pull the News Feed contents from the server on a regular basis or manually when they need it.
    * Problem 1: New data not shown until clients issue a pull request
    * Probelm 2: Most of the pull requests will be empty response if there is no new data
* Push
    * Servers push new data to the users ASA it is available
    * Long poll can make it more efficiently
        * Long poll means server only sends data when new data is available.
    * Problem 1: Celebrity user who has millions of followers. Server has to push quite frequently
* Hybrid
    * Users who have high follows to pull-based model, push data to users who have 100/1000 follows.
    * push all the users not more than a certain frequency, users with a lot of follows to regularly pull data.

## 4.12 News Feed Creation with Sharded Data

* Important requirement: create news feed to fetch the latest photos from all people the user follows.
* Need to quickly Sort photos on their time of creation, but how?
* Make photo creation time part of the photo ID.
* Make photo ID two parts: `(current epoch, auto-incrementing ID)`.
    * `auto-incrementing ID` from key-generating DB.
    * Then with PhotoID, figure out the shard number, e.g. (PhotoID % 10).
* Estimate the size of PhotoID, assume we will run the service for 50 years:
    * 86400 sec/day * 365 days * 50 yr => 1.6B sec, so 31-bit to store epoch
    * ~ 23 photos / sec, so maybe allocate 9-bit to store increment sequence.
      and reset auto incrementing sequence every second.

## 4.13 Cache and Load balancing

* Push its content closer to the user using geographically distributed photo cache servers
  and use CDNs.
* cache hot DB rows. (LRU) can be a reasonable cache eviction policy.
* 80-20 rule, try caching 20% of daily read volume of photos and metadata.

# Unit 5. Designing Dropbox

## 5.1 Why Cloud Storage

* Simplify the storage and exchange among multiple devices.
* Availability: data available anywhere, anytime. User access whenever and wherever.
* Reliability and Durability: 100% Reliability and Durability of data.
  Keeping multiple copies of the data stored on different geographically located servers.
* Scalability: Users have unlimited storage.

## 5.2 Requirements and Goals of the System

1. upload/download files/photos from any device.
2. Share files/folders with other users.
3. automatic synchronization between devices,
   i.e. updating a file on one device, all devices get synchronized.
4. Support large files up to a GB
5. ACID: atomicity, consistency, isolation and durability.
6. Offline editing. When back online, all changes should be synced to the remote servers
   and other online devices.
7. Extended Requirements: support snapshotting of the data, users can go back to any version.

## 5.3 Some Design Considerations

* Huge read write volumes.
* Read to write ratio is ~ same.
* Internally, files can be stored in small parts (e.g. 4MB).
  Failed operations shall only be retried for smaller parts of a file.
  Fails to upload a file, only the failing chunk will be retried.
* Reduce the amount of data exchange by transferring updated chunks only.
* Removing duplicate chunks, we can save storage space and BW.
* Keeping a local copy of metadata with client save a lot of round trips to the server.
* Small changes, client can intelligently upload the diffs instead of the whole chunk.

## 5.4 Capacity Estimation and Constraints

* 500 M total users, 100M daily active users.
* Average, each user connects from 3 different devices.
* On average if a user has 200 files/photos, we will have 100M total files.
* Average file size is 100K, then 100B * 100KB = 10 PB
* 1M active connections per minute.

## 5.5 High Level Design

* User will specify a folder as the workplace.
* Any file/photo/folder in this folder will be uploaded to the cloud.
* modification done on one device will propagated to all other devices

* Store files and metadata info: file name, file size, directory.
* Some servers that help clients to upload/download files.
* Some servers that can facilitate updating metadata about files & users.
* Some mechanism to notify all clients whenever update happens,
  so they can synchronize their files.


                                   |------------------------|-----------> cloud storage
         |------------------------>| block server           |
         |                         | 1, 2, 3                |--------------------
         |                         |------------------------|                   |
         |                                                                      |
         |                                                                      |
         |                                                                      |
         |                         |------------------------|                   |
         |                         | metadata server        |                   |
         |                         | 1, 2, 3                |                   V
      client---------------------> |------------------------|-----------> metadata storage
         ^                                      |
         |                                      |
         |                                      |
         |                                      V
         |                         |------------------------|
         |                         | synchronization server |
         |                         | 1, 2, 3                |
         |-----------------------> |------------------------|

* The diagram shows:
    * block server for upload/download files to/from cloud storage
    * meta data servers will keep metadata of files updates in a SQL or NoSQL
    * synchronization servers will handle the workflow of notifying all clients
      the difference

## 5.6 Component Design

### 5.6.1 Client

* Client application monitors the workplace folder, syncs all files and folders with Cloud Storage
* Client application will work with storage servers to upload, download and modify actual
  files to BE Cloud Storage
* Client application work with synchronization service to handle file metadata changes.
* Operations:
    * Upload and download files
    * Detect file changes in the workplace folder
    * Handle conflict due to offline or concurrent updates

#### 5.6.1.1 Transfer efficiently

* break each file into smaller chunks and transfer only those chunks, e.g. 4MB/chunk
* Calculate the optimal chunk
    * Storage devices we use in the cloud, input/output operations/second
    * Network BW
    * Averge file size in the storage
* Metadata to keep a record of each file and chunks that constitute it.

#### 5.6.1.2 keep a copy of metadata with Client?

* Yes! It enable us to do offline updates, also saves a lot of round trips to update remote metadata.

#### 5.6.1.3 Clients listen to changes happening with other clients?

* Solution 1: clients periodically check server for any changes.
* Probelm 1: we will have a delay in reflecting changes locally compare to server push.
    * If client checks too frequently, then waste BW.
    * Server return empty response most of the time, waste server BW.
    * Solution to this problem: long polling.

#### 5.6.1.4 The 4 parts of client:

* Internal Metadata DB: keep track of all the files/chunks/their versions/their location
* Chunker: split files into smaller chunks. reconstruct a file from its chunk
  detect the chunks that have been modified, and only transer those parts.
* Watcher: Monitor when users create/delete/update files or folders.
  also listens to any changes happening on other clients
* Indexer: process the events from watcher and update internal metadata DB with info about
  the chunks of the modified files. Once chunks are successfully submitted/download to
  the cloud, the Indexer commu. with the remote synchronization service to broadcast
  changes.

#### 5.6.1.5 Other 2 questions:

* How client handle slow servers?
    * If a server is too slow to respond, clients should delay their retries and this delay should increase
      exponentially.
* How should mobile clients sync?
    * mobile clients sync on demand to save BW and space.

               data flow           |------------------------|-----------> cloud storage
         |------------------------>| block server           |
         |                         | 1, 2, 3                |--------------------
         |                         |------------------------|                   |
         |                                                                      |
         |                                                                      |
         |                                                                      |
         |                         |------------------------|                   |
         |                         | metadata server        |                   |
         |       control flow      | 1, 2, 3                |                   V
chunker Indexer------------------> |------------------------|-----------> metadata storage
watcher Internal DB                             |
         ^                                      |
         |                                      |
         |                                      V
         |                         |------------------------|
         |                         | synchronization server |
         |                         | 1, 2, 3                |
         |-----------------------> |------------------------|

### 5.6.2 Metadata DB

* Maintaining the version and metadata info about files/chunks, users and workplaces.
* Can be SQL or NoSQL.
* Relational DB natively support ACID properties.
* Store info about the following objects.
    1. Chunks
    2. Files
    3. User
    4. Devices
    5. Workspace (sync folders)

### 5.6.3 Synchronization Service

* Process file updates made by a client and applies these changes to other clients.
* Synchronize clients' local DB with the info stored in the remote Metadata DB.
* Desktop clients commu with the synchronization service to obtain/send updates
  from/to the Cloud Storage.
* Poll the system for new updates ASA back online.
* Receives an update request, checks metadata DB for consistency and Process the update.
* A notification is sent to all subscribed users or devices to report the file update.

* Synchronization Service just transmit the difference between two versions of a file.
* Server and clients can calculate SHA-256 to decide whether to update the local chunk copy.
* Messaging middleware Between clients and the synchronization service.
    * scalable message queuing + a high number of clients using pull or push strategies.
    * Multiple synchronization service instances can receive requests from a global request Queue.

### 5.6.4 Message Queuing Service

* Supports asynchronous and loosely coupled message-based commu between distributed components of the system.
* Efficiently store any number of messages in a highly available, reliable and scalable queue.

* Request Queue is a global queue, all clients share it.
* Requests to update the metadata DB will be sent to the Request Queue first.
* Synchronization Service will take the request and update metadata.

* Response Queues that correspond to individual clients.

### 5.6.5 Cloud/Block Storage

* store chunks of files uploaded by the users.
* clients directly interact with the storage to send/receive objects.
* We separate the metadata from storage, so we can use any storage.

## 5.7 File Processing Workflow

* Scenario: ClA updates file, ClB & ClC receive update.
* If ClB & ClC are offline, they will take the Message Queueing Service

1. ClA uploads chunks to cloud storage.
2. ClA updates metadata and commits changes.
3. ClA gets confirmation and notifications are sent to ClB & C about the changes.
4. ClB and C receive metadata changes and DL updated chunks.

## 5.8 Data Deduplication

* Eliminating duplicate copies of data in storage
* Eliminating network data
* When there is an incoming chunk, we first get it's hash
  if we have the same chunk, then we don't need to receive it.

### 5.8.1 method 1 Post-process deduplication

* Receive data first, analyze later.
* Clients will not need to wait hash calculation or lookup to complete the data.
* No degradation in storage performance.
* Draw backs:
    * Store duplicate data for a short time
    * Duplicate data consuming BW.

### 5.8.2 In-line deduplication

* Calculate the hash as the clients are receiving.
* If the chunk already exists, we just need a reference, no need to store the chunk.

## 5.9 Metadata Partitioning

* M of users and B of files/chunks. We need to divide and store our data in multiple DB.

### 5.9.1 Vertical Partitioning

* One particular feature on one server.
* E.g. user related tables in one DB and files/chunks related tables in another DB.
* Issues:
* Scaling, what if we have T of chunks
* Joining two tables in separate DB can cause performance and consistency issues.

### 5.9.2 Range Based Partitioning

* Range based Partitioning
* Files start with "A" in one partition and so on
* Combine less frequently used letters into one DB partition.
* Main issue: Unbalanced servers.

### 5.9.3 Hash-Based Partitioning

* Take the hash of the "fileID" of the file object we are storing to determine the partition.
* Map the hash value to a number between [1...256].

## 5.10 Caching

* Cache for block storage: hot files/chunks.
    * Memcached will work
    * Check cache first before hitting block storage
    * A high-end server can have 144 GB of memory, so caching 36K chunks
* Cache replacement policy? LRU is good enough
* Similarly, we can have a cache for metadata DB as well.

## 5.11 Load Balancer (LB)

* Between clients and block server
* Between clients and metadata server
* Round-robin initially, but it doesn't consider load
* More intelligent LB periodically queries BE server about the load

## 5.12 Security, Permissions and File Sharing

* We will store the permissions of each file in metadata DB to reflect what files are visible
  of modifiable by any user.

# Unit 6. Designing Facebook Messenger

## 6.1 What is Facebook Messenger

* text-based instant messaging services.
* chat from cell-phones and website.

## 6.2 Requirements and Goals

### 6.2.1 Functional Requirements:

1. 1-to-1 conversations
2. track online/offline status
3. persistent storage of chat history

### 6.2.2 Non-Functional Requirements

1. real-time experience with min latency.
2. highly consistent. same chat history on all devices.
3. high availability. but can tolerate lower availability. Prefer consistency over availability.

### 6.2.3 Extended Requirements

1. Group chats
2. Push notifications

## 6.3 Capacity Estimation and Constraints

* 500M daily active users, 40 messages daily, so 20B messages per day.

### 6.3.1 Storage Estimation

* 20B messages * 100B = 2TB/day
* We store 5 yrs, 2TB * 365days * 5yr = 3.6 PB
* Also need to store users' info, messages' metadata.

### 6.3.2 BW Estimation

* 2TB/day / 86400sec ~= 25 MB/s

## 6.4 High level Design

* chat server to orchestrate communications between users.
* User1 connect to the chat server and send message to the server
* Chat server passes the message to the other user
* Chat server also stores it in the DB

        msg A                  |------------------------|                          
User1 ------------------------>|                        |
      <------------------------|                        |
        msg B                  |                        |                    
                               | chat server            |                    
        msg A                  |                        |                    
      <------------------------|                        |
User2  ----------------------> |------------------------|-----------> DB
        msg B
 
* User-A sends a message to User-B through chat server
* chat server receives the message and sends an acknowledge to User-A
* server stores the message in DB and sends the message to User-B
* User-B receives the message and sends the ack to the server
* server notifies User-A the message has been delivered successfully to User-B.

## 6.5 Detailed Component Design

* Simplified assumption: everything runs on one server.
* We need to handle:
* Receive incoming messages and deliver outgoing messages.
* Store and retrieve messages from the DB.
* Keep a record of which user is online or has gone offline, notify all the relevant users
  about the status changes.

### 6.5.1 Messages handling

* To send messages, user connect to the server and post messages.
* To get a message from the server, the user has 2 options:
    * Pull model: periodically ask the server
    * Push model: keep a connection open, server notify users.
* Pull model:
    * server needs to keep track of messages waiting to be delivered.
    * in order to minimize latency, users have to check server frequently.
    * Most of the time is empty response. So not efficient.
* Push model:
    * server doesn't need to keep track of pending messages.
    * latency is also minimized.
* How clients maintain an open connection?
    * Use HTTP long polling.
    * Server holds the request when no new data.
* How can the server keep track of the opened connection to redirect messages to the users?
    * Maintain a hash table, key is the UserID, "value" is the connection object
    * serve receives a message, looks up the user and sends the message on the open request.
* What if the server receives a message for a user who has gone offline?
    * Server notify the sender about the delivery failure.
    * If it's temporary disconnect, e.g. long-poll timed out
    * In this case, sender to retry sending messages.
    * This retry could be embedded in client's logic so users don't have to retype
    * Or server can also store the message for a while and retry sending it
      once the receiver reconnects.
* How many chat servers we need?
    * Assume 500M connections, if modern server can handle 50K connection,
      then we need 10K servers.
* How to know which server connects to which user?  
    * SW LB before chat servers, map userID to a server to redirect the request
* How should the server process a deliver message request?
    * Store the message in the DB
    * Send the message to the receiver
    * Send an ACK to the sender
    * Find the server that holds receivre connection
    * Chat server send the ACK to the sender
    * Message storing can happen in the BG
* How does the messenger maintain the sequencing of the messages?
    * Sever records the messages time stamp, but it still has problem:
    * U1 sends M1 to U2, server receives M1 at T1
    * U2 sends M2 to U1, server receives M2 at T2, T2 > T1
    * Server sends M1 to U2 and then sends M2 to U1
    * U1 sees M1 first, U2 sees M2 first
    * Keeps a sequence number with every msg for each client     
    * Although both clients see a different view of msg sequence, but the view
      will be consistent for them on all devices.

### 6.5.2 Storing and retrieving the messages from the DB.

* Can do storing msg in 2 ways:
    1. start a seperate thread, which will work with DB to store the msg.
    2. Send an async request to the DB to store the msg.
* Questions in mind:
    1. How to efficiently work with the DB connection pool
    2. How to retry failed requests
    3. Where to log those requests that failed even after some retries
    4. How to retry logged requests (repeatedly failed retries) when all the issues have resolved?
* Which storage system we should use?
    * we want to have a DB support high rate of small updates, also fetch a range of records quickly.
    * we have a huge no of small messages to insert
    * we want to sequentially access the messages
    * Cannot use MySQL or MongoDB, cannot afford to read/write every time a user receives/sends a message.
    * wide-column DB like HBase will work.
    * Column-oriented key-value NoSQL DB, multiple values against one key into multiple columns.
    * HBase groups data, store new data in a memory.
    * Once buffer is full, it dumps the data to the disk.
    * Store a lot of small data quickly, fetching rows by the key or scanning ranges of rows.
* How should clients efficiently fetch data from server?
    * Clients should paginate. Page size could be different for different clients.
    * cell phones have smaller screens.

### 6.5.3 Managing user's status

* When a user changes online/offline, we want to notify relevant users.
* But since we have 500M users, we need some optimization.
    1. client starts the app, it pulls the current status of all users in his friends' list.
    2. When a user sends a msg to an offline user, we can send a failure to the sender and update the status
    3. When a user comes online, the server broadcast with a delay in case he go offline immediately
    4. Users can pull the status from the server, this shouldn't be frequent operations
    5. When a user starts a new chat with another user, we can pull the status

### 6.5.4 Design Summary

1. Clients will open a connection to the chat server to send a message.
2. Server pass it to the requested user.
3. Active users will keep a connection open to receive messages.
4. Server push the new msg on the long poll request.
5. Msg can be stored in HBase, good for quick small updates and range based search
6. Server bcast the status of a user to other relevant users.
7. Clients can pull status.

## 6.6 Data Partitioning

* 3.6 PB for 5 yrs, has to distribute it.

### 6.6.1 Partitioning based on UserID:

* Then the data for one user is on the same DB.
* Assume each DB shard is 4TB, then we need 900 shard for 5 yrs.
* 1000 servers, then `shard No. = hashID%1000`.
* Since one user's message is on one server, it will be very fast to fetch
  the history for one user.
* At begining, we can start with multiple DB on one server.
* Then we need to know which logical partition on which server.
* As our data grows, we can add more physical servers.

### 6.6.2 Partitioning based on messageID:

* Then one user's message will be on different servers.
  It's very slow to fetch them, so do not use them.

## 6.7 Cache

* We can cache a few recent message, e.g. last 15 in a few recent conversations, e.g. 5.
* Since all the user's messages on one shard, the cache for a user should entirely
  reside on one machine too.
* See the system diagram.

## 6.8 Load balacing

* We need a load balancer that map each userID to a server that holds connection.
* We also need to a load balancer for cache servers.
* See the system diagram.

## 6.9 Fault tolerance and replication

### 6.9.1 What if chat server fails?

* Have clients automatically reconnect if the connection lost.

### 6.9.2 Should we store multiple copies of user messages?

* Yes, otherwise we have no way to recover when data crashes or server down permanently.
* We can store multiple copies of the data on different servers or use techniques
  like Reed-Solomon encoding to distribute and replicate it.

## 6.10 Extended Requirements

### 6.10.1 Group chat

* Group-chat object is identified by groupchatID and will maintain a list of people
  who are part of that chat.
* Load balancer can direct each group chat message based on groupchatID.
* The server can iterate through all the users of the chat and find the server handling
  the connection of each user to deliver the message.
* In DB, we store all the group chats in a seperate table, partitioned based on groupchatID.

### 6.10.2 Push notification

* it will enable our system to send messages to offline users.
* We need a notification server, which will take the messages for offline users.
* send them to the manufacturer's push notification server
* Then send them to the user's device.

# Unit 7. Design Twitter

## 7.1 What is Twitter?

* Users post and read short 140-char.
* Users can access through web/SMS/mobile app.

## 7.2 Requirements and Goals of the System

### 7.2.1 Functional Requirements

* Users should be able to post new tweets
* Follow other users
* Mark tweets as favorites
* Create and display a user's timeline
* contain photos and videos

### 7.2.2 Non-functional Requirements

* highly available
* 200ms for timeline generation
* Consistency can take a hit. User doesn't see a tweet for a while, should be fine.

### 7.2.3 Extended Requirements

* Searching for tweets
* Replying to a tweet
* Trending topics
* Tagging other users
* Tweet notification
* who to follow? Suggestions?
* Moments

## 7.3 Capacity Estimation and Constraints

* 1B users and 200M daily active users (DAU)
* 100M new tweets everyday
* Each user follows 200 users

### 7.3.1 How many favorites per day?

* 5 favorites / user
* 200 M * 5 = 1B favorites

### 7.3.2 How many total tweet-views will our system generate?

* each visits their timeline two times a day
* visits 5 other people's pages
* Each page sees 20 tweets
* 200M DAU * ((2+5) * 20 tweets) >= 28B/day

### 7.3.3 Storage estimates

* (140char * 2B/char + 30B metadata) * 100M = 30GB/day
* What storage needs be for 5 yrs? 30G * 365 * 5 = 54750 GB ~ 55TB
* Storage for user's data: 
* Storage for follows: (8B/UserID) * (200 following) * 1B users ~ 1600 GB ~ 1.6 TB
* Storage for favorites:
* 20% has photos and 10% has videos
* 200 KB photo, 2 MB video: 100M/5 photos * 200 KB + 100M/10 videos * 2MB ~= 24 TB/day

### 7.3.4 BW estimation

* 24TB/day upload (ingress) (audio/video) ~ 290 MB/sec
* download
    * 28B tweets * 280 B = 93 MB/s
    * 28B tweets / 5  tweets has 1 image * 200KB = 13 GB/s
    * 28B tweets / 10 tweets has 1 image / 3 videos we watch one * 2 MB = 22 GB/s
* Total ~= 35 GB/s

## 7.4 System APIs

* Post a new tweet:

```python
tweet(api_dev_key, tweet_data, tweet_location, user_location, media_ids)
```

* `api_dev_key`: the API developer key of a registered account. Throttle users based on
  their allocated quota.
* `tweet_data`: The text of the tweet, 140 chars
* `tweet_location`: (longitude, latitude) the location this tweet refers to
* `user_location`: (longitude, latitude) the location of the user
* `media_ids`: photo ids and video ids with this tweet

* Returns
    * Success: URL to access this tweet.
    * Fail: HTTP error

## 7.5 High level design

* Need to support write 100M/86400 = 1150 tweets/s
* Need to support read 28B/86400 = 325K tweets/s
* Need multiple application servers to serve all these requests
* Need load balancer to distribute traffic.
* On the BE, we need efficient DB that can:
    * store all the new tweets
    * support huge no. of reads.
* File storage to store photos and videos

                                                       |------------------------|   |-----------> file storage
                             |------------------------>| Application server     |   |
                             |                         |                        |   |
                             |                         |------------------------|   |
                             |                                                      |
                             |                                                      |
                             |                                                      |
                             |                         |------------------------|   |
                             |                         | application server     |   |
                             |                         |                        |   |
                     load    ------------------------> |------------------------|   |-----------> DB storage
clients------------> balancer                                       |               |
                             ^                                      |               |
                             |                                      |               |
                             |                                      V               |
                             |                         |------------------------|   |
                             |                         | application server     |   |
                             |                         |                        |   |
                             |-----------------------> |------------------------|   |


* 100M write + 28B read ~ 1160 write/sec + 325K read/sec
* distribute unevenly through the day
* Peak load a few thousand write + 1M read / sec

## 7.6 DB schema

* Table 1: tweet table

| PK | TweetID: int            |
|----|-------------------------|
|    | UserID: int             |
|    | Content: varchar(140)   |
|    | TweetLatitude: int      |
|    | TweetLongitude: int     |
|    | UserLatitude: int       |
|    | UserLongitude: int      |
|    | CreationDate: datetime  |
|    | NumFavorites: int       |

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

* Table 4: Favorites

| PK | TweetID: int            |
|    | UserID: int             |
|----|-------------------------|
|    | CreationDate: datetime  |

* SQL or NoSQL, refer to section 4.6

## 7.7 Data Sharding

* huge number of read/write, we need to distribute our data.
* We have multiple options to shard data.

## 7.7.1 Sharding based on UserID

* all the data of one user on one server
* Hash function that will map the user to the DB server which store
  all the tweets, favorites, follows.
* Query is similar.

* Issues:

* What if one user is too hot, a lot of queries on that server.
* Some users can have a lot of tweets or follows much more people than others
  the uniform distribution of growing user data is difficult.
* We have repartition/redistribute our data or use consistent hashing.

### 7.7.2 Sharding based on TweetID

* Map TweetID to a random server, a little bit tricky to generate timeline
* App server find all the people a user follows
* APP server send the query to all DB to find tweets from these people
* Each DB server find tweets for each user, sort them by recency
* App server will merge all the results
* This approach is good for hot user
* But we have to query all DB partitions, so higher latency
* One improvement: Cache hot tweets

### 7.7.3 Sharding based on Tweet creation time

* Advantages:
    * fetching all top tweets quickly, because we only query a very small set.
* Disadvantages: 
    * Traffic is not balancing. All writes go to one server. Most read goes to one server
    * Another, this is mine, suppose there is a user who don't post tweet for a long time
      does our app needs to go search a lot of servers? No! so this is no problem.

### 7.7.4 Combine TweetID and Tweet creation time?

* Put the timestamp into the tweetID
* TweetID = (Tweet creation epoch in second, auto increament no)
* Assume store 50 yrs, then it's 1.6B second, we need 31-bit
* Every second, we have ~1150, then we need 17-bit.
* For better performance, we use 2 DB server to generate auto-increament keys, one for even, one for odd.
* We still need to query all servers, but will be quicker
    * We don't have any secondary index, this will reduce our write latency.
    * While reading, we don't need to filter on creation-time as our primary key has epoch

## 7.8 Cache

* We can introduce a cache for DB servers for hot tweets and users.
* Memcache is a good solution

### 7.8.1 What cache replacement policy ?

* LRU can be a reasonable policy.

### 7.8.2 More intelligent cache?

* 80-20 rule, try to cache 20% of daily read volume

### 7.8.3 What if we cache the latest data?

* Delicate servers to cache all tweets from all the users from the past 3 days.
* We have 30GB of new data every day, then we need 100 GB to store for 3 days.
* Can fit into one server, but we need to distribute all the read traffic.
* When genereating timeline, we first check cache, then we check the DB.

* Hash table where 'key' would be 'OwnerID' and 'Value' would be a
  double linked list.
* This way is easy to insert and remove.

### 7.8.4 The new system diagram with LB/Sharding/Cache

|--------|                  |--------|                  |------------|
| client |----------------->| LB     |----------------->| App Server |
|--------|                  |--------|                  |------------|
                                                               |
                                                               |
                                                               |
                                                               v
|--------------|                                        |-------------------------|
| File Storage |<---------------------------------------| Aggratator Server 1/2/3 |
|--------------|                                        |-------------------------|
   |                                                      |        |
   |       |--------|                                     |        |
   |       | LB     |<------------------------------------|        |
   |       |--------|                                              |
   |          |                                                    |
   |          |                                                    |
   V          V                                                    V
|--------------------|                                  |-------------------------|
| Cache Server 1/2/3 |<---------------------------------| DB Server 1/2/3...N     |
|--------------------|                                  |-------------------------|

## 7.9 Timeline Generation

* Refer to Facebook's Newsfeed.

## 7.10 Replication and Fault Tolerance

* Read-heavy system, we have multiple secondary DB servers for each DB partition.
* secondary DB servers for read only
* Writes go to the primary server, then replicated to secondary servers.
* It gives us fault tolerance. When ever primary server goes down, we can failover to a secondary server.

## 7.11 Load Balancing

* Add load balancing at 3 places in our system:

1. Between Clients and Application servers.
2. Between Application servers and DB replication servers.
3. Between Aggregation servers and Cache server.

* Initially the Round Robin is good enough.
* Still Round Robin doesn't consider load
* More intelligent LB that queries BE server load.

## 7.12 Monitoring

* We need to collect following metrics/counters
1. New tweets per day/second, what is daily peak?
2. Timeline delivery stats, how many tweets per day/second is delivering?
3. Average latency to refresh timeline?

## 7.13 Extended Requirements

### 7.13.1 How do we serve feeds?

* Only fetch top N tweets
* Depends client's Viewport, mobile show fewer tweets compare to a Web client.
* We can also cache next top tweets
* We can also pre-generate the feed, see 4.11.1

### 7.13.2 Retweet

* If retweet, we just need to store the ID of the original Tweet
  not the content

### 7.13.3 Trending topics

* Cache most frequently occuring hashtags or search queries in the last N seconds.
* Ranking based on frequency of tweets or search queries or retweets or likes.
* We can give more weight to topics that shown to more people.

### 7.13.4 Who to follow? How to give Suggestions?

* Suggest friends of follows
* We can go two or three levels down to find famous people.
* Use ML to give score to each user, inputs will be common followers, common location
  or interests, etc.

### 7.13.5 Moments

* Get top news
* Figure out related tweets, categorize them, prioritize them.
* Show these articles.

### 7.13.6 Search

* See section "Design Twitter Search"

# Unit 8 Designing Youtube or Netflix

* Similar service: youtube.com/netflix.com/vimeo.com/dailymotion.com/veoh.com

## 8.2 Requirements and Goals of the System

### 8.2.1 Functional Requirements

* Users should be able to upload videos
* Users should be able to share and view videos
* Users should be able to perform and searches based on video titles
* Our service should be able to record stats, likes/dislikes, total no. of views.
* Users should be able to add and view Comments on videos.

### 8.2.2 Non-Functional Requirements

* Highly reliable, video should not be lost
* Highly available, Consistency can take a hit, if user doesn't see a video for a while, should be fine
* Users should have a real time experience, should not feel any lag.

### 8.2.3 Not in scope

* Video recommendations
* Most popular videos
* Channels
* Subscriptions
* Watch later
* Favorites

## 8.3 Capacity Estimation and Constraints

* 1.5B total users, 800M DAU
* 5 videos per day, total video-view / sec is: 800M * 5 / 86400 = 46K videos/sec
* upload/download ratio is 1:200, 46K / 200 = 230 videos/sec

### 8.3.1 Storage Estimates

* 500 hours/min videos are uploaded to Youtube. 1 Min video needs 50MB
* 500 hrs * 60 min * 50 MB ~ 1500 GB/min = 25 GB/sec
* Video compression and replication would change our estimates

### 8.3.2 BW estimates

* Each video upload takes a BW of 10 MB/min
* 500 hrs * 60 mins * 10 MB = 300 GB/min
* Since upload:view ratio is 1:200, we would need 1TB/s outgoing BW.

## 8.4 System APIs

* uploading API

```python
uploadVideo(api_dev_key, video_title, video_desc, tags[], category_id, default_lang, recording_details, video_contents)
```

* `api_dev_key`: the API developer key of a registered account. Throttle users based on
  their allocated quota.
* `video_title`: title of the video
* `video_desc`: optional desc of the video
* `tags`: optional tags for the video
* `category_id`: Category of the video, e.g. Film/Song/People
* `default_lang`: En/Ch/Fr
* `recording_details`: Location where the video was recorded
* `video_contents`: Video to be uploaded

* Returns
    * Success, HTTP 202, A link to the video
    * Or queryable API

```python
searchVideo(api_dev_key, search_query, user_location, maximum_videos_to_return, page_token)
```

* `api_dev_key`: the API developer key of a registered account. Throttle users based on
  their allocated quota.
* `search_query`: String containing the search terms
* `user_location`: Location of the user performing the search
* `maximum_videos_to_return`: Max no of results returned in one request.
* `page_token`: specify a page in the result set that should be returned

* Returns (JSON): containing info about the list of video resources matching the search query
  Will have a video title, a thumbnail, video creation date and view count

```python
streamVideo(api_dev_key, video_id, offset, codec, resolution)
```

* `api_dev_key`: the API developer key of a registered account. Throttle users based on
  their allocated quota.
* `video_id`: A string to identify the video
* `offset`: a time in seconds from the beginning of the video. 
  we can support play/pause from multiple devices. User can watch video on any device where they left off. 
* `codec`: send codec and resolution in the API from client to support multiple devices
  First watch on the TV, then watch on a phone.

* Returns: A media stream (a video chunk) from the given offset.

## 8.5 High level Design

* High level components are like following
* Processing Queue: uploaded video will be pushed into it and de-queued later for encodeding/thumbnail generation and storage
* Encoder: to encode each uploaded video into multiple formats
* Thunbnails generator: to generate a few thumbnails for each video.
* Video and thumbnail storage: To store video and thumbnail files in some distributed file storage.
* User DB: To store user's info, e.g., name, email, address, etc.
* Video metadata storage: A metadata DB to store all the info about video
    * title
    * file path
    * uploading user
    * total views
    * likes
    * dislikes
    * Video Comments

|--------|                  |------------|                  |-------------------|                        |------------------|                        |--------|
| client |<---------------->| Web server |<---------------->| App Server        |----------------------->| Processing Queue |----------------------->| Encode |
|--------|                  |------------|                  |-------------------|                        |------------------|                        |--------|
                                                               ^      ^      ^                                                                           |  |
                                                               |      |      |                          |-------------------------------------------------  |
                                                               |      |      |------------------------------------------------|                             |                             
                                                               v      |                                 |                     |                             |                              
                                                        |---------|   |              |-------------|    |             |---------------------------|         |
                                                        | User DB |   |------------->| Metadata DB |<---|             | video & thumbnail storage |<--------|
                                                        |---------|                  |-------------|                  |---------------------------|
 
## 8.6 DB Schema

### 8.6.1 Video meta storage - MySQL

* VideoID
* Title
* Description
* Size
* Thumbnail
* Uploader/User
* Total number of likes
* Total number of dislikes
* Total number of views

* For each video Comment
    * CommentID
    * VideoID
    * UserID
    * Comment
    * TimeOfCreation

### 8.6.2 User data storage - MySQL

* UserID, Name, email, address, age, registration details etc.

## 8.7 Detailed Component Design

* Read heavy system, 200:1

### 8.7.1 Where would videos be stored?

* Distributed file storage system like HDFS or GlusterFS.

### 8.7.2 How should we efficiently manage read traffic?

* Segregate read traffic from write traffic
* We have multiple copies of each video, so distribute our read traffic on different servers.
* Metadata, we can have a master-slave configuration: writes go to master first then applied to slaves.
* Will cause some staleness, when slaves' metadata is not in sync with the master
* This staleness is short and acceptable

### 8.7.3 Where to store thumbnails?

* Assume each video has 5 thumbnails.
* We need to have efficient storage that servers huge read traffic
* Each thumbnail is small, 5KB each
* Read traffic for thumbnail will be huge compare to video, since one web page can 20 videos, each of them have 5 thumbnails.
* If we store them on a disk, we have to perform a lot of seeks to different Location on the disk to read these files, inefficient!
* Bigtable is an ideal choice
    * since it combines multiple files into one block to store on the disk.
    * Very efficient in reading a small amount of data.
* We can also cache hot thumbnails, since they are small, we can cache a lot of them.

### 8.7.4 video uploads

* We should support resumming from the same point

### 8.7.5 video encoding

* Once video is uploaded, then put them into a queue for encoding
* Once encoding is completed, the user will be notified and video will be made available for view/sharing.


                                                                 |---------|                  |-------------|    
                                                                 | User DB |  |-------------->| Metadata DB |<-------------------------------------------
                                                                 |---------|  |               |-------------|                                           |
                                                                      |       |                                                                         | 
                                                                      |       |                                                                         | 
                                                                      |       |                                                                         | 
                                                                      v       v                                                                         v 
|--------|                  |------------|                  |-------------------|                        |------------------|                        |--------|
| client |<---------------->| Web server |<---------------->| App Server        |----------------------->| Processing Queue |----------------------->| Encode |
|--------|                  |------------|                  |-------------------|                        |------------------|                        |--------|
    ^                             ^                                          ^                                                                           |  |
    |                             |                                          |                          |-------------------------------------------------  |
    |                             |                                          |------------------------------------------------|                             |                             
    |                             |                                                                     |                     |                             |                              
    |                             |                                                                     |                     |                             |                              
    |                             |                                                                     |                     |                             |                              
    |                             |                                                                     |                     |                             |                              
    |                             v                                                                     |                     |                             |                              
|-----------|              |-------------------|                                     |---------------|  |             |----------------------------|        |
|  CDN      |<-------------| Video Image Cache |<------------------------------------| Video storage |<-|             | Bigtable thumbnail storage |<-------|
|-----------|              |-------------------|                                     |---------------|                |----------------------------|
 
## 8.8 Metadata Sharding

* We need to distribute our data on multiple machines

### 8.8.1 Based on UserID

* Pass UserID to hash function, map the user to DB server.
* To search video by titles, we will query all servers and each server will return a set of videos.
* A centralized server will aggregate the rank and return to user

#### Issues with this approach

* If a user is too hot, then a lot of queries on the server, creating bottlenecks.
* Some users store much more videos than others, it's hard to maintain uniform distribution.
* We have repartition/redistribute our data or use consistent hashing.

### 8.8.2 Based on Video ID

* Just map the videoID to a server
* Search still needs to query all servers
* Shifts the popular user problem to popular video.
* Using cache to store hot videos.

## 8.9 Video Deduplication

* Huge no of user, massive amount of video, we need to deal with widespread video duplication.
* duplication differ in aspect ratio, encoding, contain overlays or additional border, excerpts from a longer video.
* Wasting data storage, degrade cache efficiency, increase network traffic and energy consumption.
* Users will also see duplicate search results, longer video startup times
* We are trying to find duplication when a user is uploading a video.
* We can run video matching algorithms, e.g. block matching, phase correlation.
* If we find a video already being uploaded, we can stop upload or use existing copy or user higher quality.
* If the new uploaded video is a subpart, we can divide the video into smaller chunks.

## 8.10 Load Balancing

* We use consistent Hashing among cache servers, so the load between cache servers will be balanced.
* If a video becomes popular, it's logical partition will have more traffic.
* Busy server in one Location can redirect to a client to a less busy server in the same cache location.

* Problems: if the host can't serve the video. Each redirection requires a client to make an additional HTTP
* Higher delays before video playing back.
* cross data-center redirections lead a client to a distant cache.

## 8.11 Cache

* Use a large number of geographically distributed video cache
* We need maximize user performance and evenly distributes the load on cache servers.
* Cache for metadata servers
* Using Memcache
* Use LRU policy
* Use 80-20 rule

## 8.12 Content Delivery Network (CDN)

* deliver web content based in the geographical locations
* Check out "CDN" in caching chapter
* Move popular videos to CDN
    * CDNs replicate content in multiple places.
    * CDN make heavy use of caching

## 8.13 Fault Tolerance

* Consistent Hashing: distribution among DB servers.
* Help replacing dead server, also help in distributing load among servers.

# Unit 9 Designing Typeahead Suggestion

* Similar Services: Auto-Suggestions, Typeahead search
* Difficulty: Medium

## 9.1 What is Typeahead Suggestion?

* Users search for known and frequently searched terms
* When user types into the search box, it tries to predict the query based on the characters
  the user has entered and gives a list of Suggestions
* It's about guiding the users to construct their search query.

## 9.2 Requirement and Goals of the system

* Functional Requirements: As the user types in their query, our service should suggest top 10 terms starting
  with whatever the user has typed.
* Non-functional Requirements: The Suggestions should appear in real-time.
  The user should be able to see the suggestion within 200ms.

## 9.3 Basic System Design and Algorithm

* We need to store in such a way, users can search with any prefix
    * E.g. systems contains `[cap, cat, captain, capital]`, the user has typed in
      `cap`, then the system suggests `[cap, captain, capital]`
* We need highly efficient data structure, i.e. `Trie`
    * We can even merge the node with one branch to save storage
* Case insensitive? For simplicity, assume our data is case insensitive.
* How to find top suggestion?
    * We can record the count of seraches, e.g. CAPTAIN 100 times and CAPTION 500 times
    * When search, we find the top suggestions for a given prefix, we can traverse the sub-tree
* Given a prefix, how much time will it take to traverse its sub-tree?
    * We expect huge tree, and strict latency requirements, we do need to improve efficiency.
* Can we store top suggestions with each node?
    * Surely will speed up searches but will require a lot extra storage.
    * We can store 10 suggestions at each node, but just storing references of the terminal nodes.
    * Why we need to traverse back using the parent reference?
    * Also store the frequency with each reference to keep track of top suggestions.

### 9.3.1 How to update the trie?

* 5B searches everyday, we would have 60K queries/second, very resource intensive and will hamper our read requests.
* We need to update our trie offline after a certain interval.
* When new queries come in, we log them and track their frequencies. We can do this every 1000 query.
* We can use Map-Reduce (MR) to process all the logging data every hour. These MR jobs
  will calculate frequencies of all searched terms in the past hour.
* We need to update the Trie offline, so won't jog the reading requests.
    * We can make a copy of the trie on each server to update it offline. Once done we can switch 
      to start using it and discard the old one.
    * We can have a master-slave configuration, master is serving traffic, slave gets the update.
      Then switch master and slave.

### 9.3.2 How can we update the frequencies of typehead suggestions?

* We will keeping counting all the terms in last 10 days, and add it with exponential moving average (EMA).
  We give more weight to the lastest data.
* After inserting a new term, it's possible this term jumped into the top 10 queries for a few other nodes.
* We go from root and check if the current query's frequency is high enough to be top 10.
* If so, we insert this new term and remove the term with the lowest frequency.

### 9.3.3 How can we remove a term from the trie?

* The reason to remove: legal issue/hate/piracy.
* We can do it when the regular update happens.
* Or we can add a filtering layer on each server, which will remove any such term before sending them to users.

### 9.3.4 Different ranking criteria?

* Freshness, user location, language, demographics, personal history.

## 9.4 Permanent Storage of the Trie

### 9.4.1 How to store trie in file so we can rebuild easily?

* Take a snapshot periodically and store it in a file.
* We can store the tree serilized, the node followed by how many children it has, e.g. "C2,A2,R1,T,P,O1,D"
* There is no easy way to store the top suggestions for each node, how to recalculate it.

## 9.5 Scale Estimation

* Service like Google: 5B searches everyday, ~60K/sec queries.
* We can assume only 20% will be unique, assume we only want to index the top 50%
* Then we assume we will have 100M unique terms

### 9.5.1 Storage Estimation:

* On average, each query consists of 3 words and the average length of a word is 5 chars
* We will have 15 chars of average query size, we will need 30 bytes to store an average query.
* Total storage we will need is 100M * 30 bytes >= 3 GB.
* If we expect 2% new queries everyday and maintaining our index for the last year, total storage we should expect: 3 GB + (0.02 * 3GB * 365 days) ~ 25 GB

## 9.6 Data Partition

* Although the data can easily fit in one server, we can still partition them to lower latencies.

### 9.6.1 Range Based Partition

* We can store based on the first letter.
* Combine less frequently occurring letters into one partition.
* The problem is still Unbalanced servers. E.g.
    * Put all terms starting with "E" in one partition
    * Later we found there are too many terms and we can't fit into one partition.

### 9.6.2 Partition based on the maximum capacity of the server

* Whenever a sub-tree cannot fit into a server, we break our partition there to assign that range to this server, e.g.
    * Server 1: A-AABC
    * Server 2: AABD-BXA
    * Server 3: BXB-CDA
* When user type "AA", we have to query Server 1 and 2. But when the user typed "AAA", we only need to query server 1.
* We can have a load balancer in front of trie servers to store this mapping and redirect traffic.
* Either server side or client side need to merge results.
* Can still have hot spot problem.

### 9.6.3 partition based on the hash of the term

* The distribution of the term will be more balanced.
* The disadvantage is we have to query all servers to aggregate results.

## 9.7 Cache

* We should have separate cache servers in front of the trie servers holding most frequently searched terms and their typehead suggestions.
* Application servers should check these cache servers before hitting the trie servers.
* ML model based on simple counting, Personalization, or trending data.

## 9.8 Replication and Load balancer

* We should have replicas for trie servers for load balacing and fault tolerance.
* We need load balancer to track data partitioning scheme.

## 9.9 Fault Tolerance

* What if a trie server goes down? We can have a master-slave configuration.
* If the master dies, the slave can take over.
* Server comes back up, can rebuild the trie based on the last snapshot.

## 9.10 Typeahead Client

* The following optimization on the client side to improve user's experience.
* The client only hit server if User has not pressed any key for 50ms.
* If the user is constantly typing, the client should cancel the in-progress requests.
* Initially, the client can wait until the user enters a couple of characters.
* Clients can pre-fetch some data from the server to save future requests.
* Clients can store the recent history of suggestions locally. Recent history has a very high rate of being reused.
* As soon as the user opens the search engine website, the client can open a connection with the server.
* The server can push some part of their cache to CDN and Internet Service Providers for efficiency.

## 9.11 Personalization

* User will receive suggestions based on historical searches, location, language.
* We can store personal history of each user separately on the server.
* Also cache them on the client.
* The server can add personalized terms and send them to the user.

# Unit 10 Designing an API Rate Limiter

* Design an API Rate Limiter which will throttle users based upon the number the requests they are sending.
* Difficulty Level: Medium.

## 10.1 What is a Rate Limiter?

* Our service receives a huge number of requests, we cannot serve them all.
* We need some rate limiting mechanism which only allow certain number of requests.
* RL can do:
    * A user can send only one message per second.
    * A user is only allowed 3 failed transactions per day.
    * A single IP can only create 20 accounts per day.
* RL caps how many requests a sender can issue. After caps reached, RL blocks further requests.

## 10.2 Why do we need API RL?

* Protect us against abusive behaviors
    * like DOS attacks
    * brute-force password/credit card
* Hard to detect
* Easily bring down the server

### 10.2.1 Beneficial Scenario

* Mishehaving clients/scripts
    * Users can send a log of low-priority requests.
* Security: They are only allowed to try a certain times of wrong password.
* Prevent abusive behaviors:
    * Users requests the same info again and again
* Keep costs and resource usage under control.
* Revenue: Premium users and normal user charge differently.
* Eliminate spikiness in traffic

## 10.3 Requirement and Goals of the system

### 10.3.1 Functional Requirements

* Limit the # of requests an entity can send to an API within a time window, e.g. 15 requests/sec.
* The user should get an error message when threshold is crossed within single server or across a combination of servers.

### 10.3.2 Non-Functional Requirements

* Highly available, RL should always work since it protects the service.
* Should not introduce substantial latencies affecting the user experience.

## 10.4 How to do Rate Limiting

* RL is a process to define the rate and speed at which consumers can access APIs.
* Throttling is to control the usage during a given period.
* Throttling can be at the application level and/or API level.
* When limit is crossed, server returns HTTP 429 - Too many requests.

## 10.5 What are different types of throttling?

* Hard Throttling: the no of API requests cannot exceed the throttle limit.
* Soft Throttling: API request limit to exceed a certain percentage.
  E.g., we limit to 100 messages and allow 10% exceed-limit, we allow 110 message.
* Elastic of Dynamic Throttling: can go beyond the threshold if the system has some resources

## 10.6 What are different types of algorithms used for RL?

### 10.6.1 Fixed Window Algorithm

* E.g., if the window is 1 second, the `[0,1]` and `[1,2]` are two windows`

### 10.6.2 Rolling Window Algorithm

* The window starts when the first request is made.

## 10.7 High level design for Rate Limiter

* RL decides which request will be served by the API.
* Web Server arrives first, then web server asks the RL to decide to server or throttle.
* If we decide to serve, then request goes to API servers.

|--------|                  |------------|                  |-------------------|
| client |<---------------->| Web server |<---------------->| App Server 1/2/3  |
|--------|                  |------------|                  |-------------------|
                                  ^             
                                  |             
                                  |             
                                  |             
                                  |             
                                  |             
                                  |             
                                  v             
|------------|              |-------------------|              |-------------------|
| BE Storage |<-------------| Rate Limiter      |------------->| Cache server      |
|------------|              |-------------------|              |-------------------|

## 10.8 Basic System Design and Algorithm

* Limit the number of requests per user.
* For each unique user, we would keep a count representing how many requests the user
  has made and a timestamp when we started counting.
* We can keep the in a hashtable: `{UserID: [Count, EpochTime]}`
* Assume the RL is 3 requests/min
* When a new request comes in, we will perform the following steps:
    * If `UserID` is not present in the hash-table, insert it, set the `Count` to 1
      set `StartTime` to the current time, round to minute.
    * Otherwise, find the `UserID`. if `CurrentTime - StartTime >= 1 min`,
      set the `StartTime` to the CurrentTime, set `Count` to 1, allow request
    * If `CurrentTime - StartTime <= 1 min` and if `Count < 3`, increament the Count and allow the request.
      If `Count >= 3`, reject the request.

### 10.8.1 Problems with this algorithm.

1. This is a Fixed Window algorithm. A User can potentially have 6 requests in one min window.
2. Atomicity: A user's Count is 2, and she sends 2 more requests. Two separate processes served each requests.
   and they concurrently read the count before they updated it.
    * If we use Redis to store the key-value, we can use Redis lock
    * If we are using a simple hash-table, we can have a custom implementation for 'locking'
3. How much memory would we need to store all of the user data?
    * `UserID`: 8 bytes, `Count`: 2 bytes, `epoch time`: 2 bytes enough for min+second part.
    * 20 bytes for each record.
    * 1M users at any time: (12+20) bytes * 1M => 32 MB.
    * 4-byte lock for each record, 32 MB + 4MB = 36 MB.
    * We still want to distribute the data, we will store them in Redis or Memcached.
    * We store the all the data in the remote Redis servers and all RL will read these servers
      before serving or throttling any request.

## 10.9 Sliding Window algorithm

* We can maintain a sliding window.
* Store the timestamp of each request in Redis `Sorted Set` in `value` field of hash-table.
* Here are the steps:
    1. Remove all the timestamps from the Sorted Set that are older than "CurrentTime - 1 min"
    2. Count the total number of elements in the sorted set. Reject if this count is >= 3
    3. Insert the current time in the sorted set and accept the request.
* How much memory would we need?
    * `UserID`: 8 bytes, `epoch time`: 4 bytes.
    * 20 bytes overhead for each sorted set element in hashtable and 20 bytes for hashtable
    * 8+(4+20)*500+20 = 12 KB
    * sorted set element use linklist, one ptr to previous one, one ptr to next one. Each ptr is 8-byte,
      then plus 4-byte for other overhead. Then we come up with 20 ptr.
    * If we need to track 1M users, total memory is 12 KB * 1M ~= 12 GB

## 10.10 Sliding Window with Counters

* Assume we have hourly limit, we can keep a count for each min and calculate the sum.
* Example: 500 requests/hour, 10 requests/min
* Store the counters in a Redis Hash, because it's very efficient for fewer than 100 keys.
* When each request increaments a counter, it also sets the hash to expire an hour later.
* We will normalize each "time" to a minute.

### 10.10.1 How much memory we would need?

* `UserID`: 8 bytes, `epoch time`: 4 bytes, `Counter`: 2 bytes
* 20 bytes overhead for hash-table and 20 bytes for Redis hash.
* Since we'll keep a count for each min, we would need at most 60 entries
* 8 + (4+2+20)*60 + 20 = 1.6 KB, 1M users ~= 1.6 GB, save 86% memory compare to sliding window algorithm.

## 10.11 Data Sharding and Caching

* We can shard based on the "UserID" to distribute the user's data.
* For fault tolerance and replication we should use consistent Hashing.
* We can also shard per uer per API, e.g. we have different RL for `createURL()` and `deleteURL()`.
* We want to limit each user not to create more than 100 short URLs per hour.
* Assume we are using Hash-Based Partition for `createURL` API, we can rate limit each partition to
  allow a user to create not more than 3 per minute.

### Cache

* Application servers can quickly check if the cache has the desired record.
* We can benefit from the Write-back cache by updating all counters and timestamps in cache only.
* This way latency is minimized.
* We can use (LRU)
 
## 10.12 Should we rate limit by IP or by user?

### IP

* multiple users share a single public IP in an internet cafe.
* Bad users can throttle other users.
* Another Problem: run out of memory tracking IPv6 address.

### User

* After ahthentication, user will be provided with a token which is used in every request.
* A hacker can perform a denial of service attack by entering wrong credentials up to the limit.
  Then user can not log in.

### Hybrid

* Do both per-IP and per-user rate limiting
* More cache entries with more details per entry, more memory and storage.

# Unit 11 Designing Twittr Search

* Design a service that can store and search user tweets.
* Difficulty Level: Medium

## 11.1 What is Twittr Search?

* Our goal is to design system that allows searching over all the user tweets.

## 11.2 Requirements and Goals of the System?

* 1.5 B total users with 800 M DAU
* 400 M tweets every day
* 300 Bytes per tweet
* 500 M searches every day.
* multiple words combined with AND/OR.
* We need to design a system that can efficiently store and query tweets.

## 11.3 Capacity Estimation and Constraints

* Storage Capacity: 400M * 300 >= 120 GB/day ~= 1.38 MB/sec

## 11.4 Systems APIs

```python
search(api_dev_key, search_terms, maximum_results_to_return, sort, page_token)
```

* `api_dev_key`: the API developer key of a registered account. Throttle users based on
  their allocated quota.
* `search_terms`: A string containing the search terms
* `maximum_results_to_return`: # of tweets to return.
* `sort`: sort mode, 0 - latest first, 1 - Best matched, 3 - Most liked.
* `page_token`: specify a page in the result set that should be returned.

* Returns: A JSON containing info about a list of tweets matching the search query
    * containing user ID & name
    * tweet text
    * tweet ID
    * creation time
    * # of likes.

## 11.5 High Level Design

* We need to build an index that can keep track of which word appears in which tweet

|--------|  Update Status   |------------|                  |-------------------|
| client |<---------------->| App server |<---------------->| Storage Server    |
|--------|  Search Status   |------------|                  |-------------------|
                                  ^             
                                  |             
                                  |             
                                  |             
                                  |             
                                  |             
                                  |             
                                  v             
                            |-------------------|
                            | Index Server      |
                            |-------------------|

## 11.6 Detailed

### 11.6.1 Storage

* We need to store 120G of new data every day.
* So we need data partitioning scheme 
* If we plan for next 5 years, we need 120G * 365 days * 5 yrs ~= 200 TB.
* We only want to 80% full, we need 250 TB.
* Assume we need an extra copy, then we need 500 TB.
* Assume modern server can hold 4T, then we need 125 servers.
* Assume we use MySQL, store 2 columns: TweetID and TweetText.
* Hash function to map TweetID to a storage server.

#### 11.6.1.1 How to create system-wide unique TweetIDs?

* 400M * 365 days * 5 yrs => 730 B
* We need 5 bytes and generate a unique TweetID, similar to "Designing Twitter"

#### 11.6.1.2 Index

* Assume we have 300K English words and 200K nouns
* Assume 5 chars average for each word, then we need 2.5 MB memory
* Want to keep the index in memory for all tweets from only past 2 years, i.e. 292B tweets.
* Each TweetID will be 5B, then we need to store 1460 GB.
* Our index would be a big distributeed hash table
* key would be the word, value will be a list of TweetIDs of all tweets contain that word.
* Assume we have 15 words in each tweet to be indexed.
* So total memroy (1460 * 15) + 2.5MB ~= 21 TB.
* Assuming a high-end serve has 144 GB of memory, we would need 152 such servers to hold our index.

#### 11.6.1.3 Sharding based on Words

* Iterate through all the words of a tweet and calculate the hash and find the server.
* To Query, we only need to query only one server.
* Again, what if a word becomes hot? Server will be hot.
* Some words can store a lot of TweetIDs than other words, so distribution is not unique.

#### 11.6.1.4 Sharding based on tweet object

* We generate hash for TweetID, and store all the words of the tweet on that server.
* To query, we have to query all the servers.
* A centralized server will aggregate the results.

|--------|     |------|     |------------|
| client |---->| LB   |---->| App server |
|--------|     |------|     |------------|
                                  ^             
                                  |             
                                  |             
                                  |             
                                  |             
                                  |             
                                  |             
                                  v             
                            |-------------------|                  |-------------------|
                            | aggregator Server |<---------------->| DB 1/2/3/4/5      |
                            | 1/2/3             |                  |                   |
                            |-------------------|                  |-------------------|
                                   |                                     |
                                   |                                     |
                                   |                                     |
                                   v                                     v
                            |-------------------|                  |----------------------|
                            | Index Server      |<---------------->| Index Builder Server |
                            | 1/2/3             |                  |                      |
                            |-------------------|                  |----------------------|

## 11.7 Fault Tolerance

* What will happen when a image server die?
    * We can have a secondary replica of each server.
    * Primary dies, then secondary takes over.
* What if both dies? Need to rebuild the same index on it.
    * Brutal force way is to iterate all DB
    * Filter tweet based on hash function
    * inefficient
    * During rebuild, we can't serve any query.
* How to retrieve mapping between tweets and the index server?
    * Build a hash table
    * Key will be the index server number, value will be a Hashset containing all the TweetIDs.
    * When a index server crahes, we can quickly get all the tweets
    * We should also have a replica of the Index-Builder server

## 11.8 Cache

* We can introduce a cache in front of our DB.
* We can use Memcached.
* We can use LRU.

## 11.9 LB

* Between Clients and APP servers
* Between App servers and BE servers
* A RR in the begining
* Later might need LB based on load.

## 11.10 Ranking

* Rank by social graph distance, popularity relevance?
* We store (# of likes) and store it with the index.
* Each partition do the sorting and sends to aggregator.
* Aggregator Combines all these results.

# Unit 12 Designing a Web Crawler

* Web Crawler systematically browse and download the WWW.

## 12.1 What is a Web Crawler

* A Program which browses the WWW.
* It revursively fetching links from a set of starting pages
* Search engines download all the pages to create an index on them to perform faster searches.
* To test Web pages and links for valid syntax and structure
* To monitor sites to see when their structure or contents change
* Maintain mirror sites for popular Web sites.
* Search for copyright infringement
* To build a special-purpose index.

## 12.2 Requirements and Goals of the System

* Scalability: can crawl the entire Web and can be used to fetch hundreds of millions of Web doc.
* Extensibility: should be designed in a modular way that new functionality will be added to it.
  Newer doc types that need to be downloaded.

## 12.3 Some Design Considerations

* Is it a crawler for HTML pages only? Should we fetch and store other types of media, sound/images/videos?
  We want to break parsing module into different sets of modules: HTML/images/videos
* We will assume HTTP, no FTP, but it should be extended.
* What is the expected number of pages? How big will the URL database become.
    * Assume 1B websites
    * Assume 15B web pages we will reach
* What is 'RobotExclusion' and how should we deal with it?
    * Webmasters declare parts of their sites off-limits to crawlers.

## 12.4 Capacity Estimation and Constraints

* We want to crawl 15 B pages in 4 weeks, then ~ 6200 pages/sec
* What about storage?
    * Since we only process HTML, we assume the average page size of 100 KB, and store 500 bytes of metadata
    * 15B * (100KB + 500) ~= 1.5 petabytes
    * Assume 70% capacity model, and we don't want to go above 70%, so 1.5 petabytes / 0.7 ~= 2.14 petabytes.

## 12.5 High Level design

* Take a list of seed URLs as its input and repeatedly execute the following steps
    1. Pick a URL from the unvisited URL list
    2. Determine the IP Address of its host-name
    3. Establish a connection to the host to download the corresponding document.
    4. Parse the document contents to look for new URLs.
    5. Add the new URLs to the list of unvisited URLs.
    6. Process the downloaded document, e.g., store it or index its contents.
    7. Go back to step 1

### 12.5.1 How to crawl?

* BFS and DFS? BFS usually used, sometimes DFS
* Path-ascending crawling: ascend to every path in each URL
    * e.g. `foo.com/a/b/page.html`, `foo.com/a/b`, `foo.com/a`, `foo.com`

### 12.5.2 Difficulties in implementing efficient web crawler

* Large volume of Web pages: web crawler can only download a fraction of the web pages
  web crawler should prioritize download
* Rate of chage on web pages, web page change very frequently.
* components needed for min crawler
    * 1. URL frontier: store the list of URLs to download and also prioritize which URLs crawled first.
    * 2. HTML Fetcher: to retrieve a web page from the server.
    * 3. Extractor: to extract links from HTML documents.
    * 4. Duplicate Eliminator: to make sure the same content is not extracted twice
    * 5. Datastore: To store retrieved pages, URLs, and other metadata.

## 12.6 Detailed Component Design

* Assume our crawler is running on one server
* crawling is done by multiple working threads

### 12.6.1 step1

* Remove an absolute URL from the shared URL frontier for downloading.
* An absolute URL begins with a scheme "HTTP/FTP", which identifies the network protocol
* Based on the protocol, the worker calls the appropriate module to download.
* After downloading, the document is placed into a Document Input Stream (DIS)

### 12.6.2 step2

* the worker thread invokes the dedupe test to determine
  if the URL has been seen before.
* If so, move to next URL.

### 12.6.3 step3

* Process the DL doc.
* Each can have different MIME type like HTML page, Image/Video.
* Implement in a modular way, can be extended to future types.

### 12.6.3 step4

* Futhermore, HTML processing module will extract all links.
* Run through user-supplied URL to filter
* Checks if the URLs has been seen before, if not download it.


                                        |------------------|       |-------------|
                                        | Queue Files      |       | URL set     |
                                        |------------------|       |-------------|
                                                 ^                        ^
                                                 |                        |
                                                 |                        |
                                                 V                        |
                 |----------------|     |------------------|       |------------|
    ------------>| DNS Resolver   |     | URL Frontier     |<------| URL De-Dup |
    |            |----------------|     |------------------|       |------------|
    |                  ^                      ^                            ^
    |                  |      |---------------|                            |--------------------|
    |                  |      |                                                                 |
    V                  V      V                                                                 V
|----------|     |----------------|     |------------------|     |------------------|     |------------|
| Internet |---->| HTML Fetcher   |---->| Doc Input Stream |---->| Extractor        |---->| URL Filter |
|----------|     |----------------|     |------------------|     |------------------|     |------------|
                                                 |
                                                 V
                                        |------------------|     |-----------|
                                        | Doc De-dup       |---->| Doc Store |
                                        |------------------|     |-----------|
                                                 |
                                                 V
                                        |------------------|
                                        | Doc checksum set |
                                        |------------------|

#### 12.6.4.1 The URL frontier

* It contains all the URLs that remain to be DL.
* Perform BFS. Use FIFO to implement.
* We have a huge list to crawl, we can distribute our URL frontier into multiple servers.
* Each server we have multiple worker threads performing the crawling tasks.
* Hash function maps each URL to a server.
* Politeness requirements:
    * Crawler should not overload a server.
    * We should not have multiple machines connecting a web server.
* Each server and Each worker will have its seperate sub-queue.
* How big will our URL frontier be?
    * millions of URLs, so we have to use disks
    * We can have separate buffers for enqueuing and dequeuing.
    * Enqueuing buffer once filled will be dumped to the disk.
    * Dequeuing buffer will periodically read from disk to fill the buffer.

#### 12.6.4.2 The fetcher module

* Download the document using appropriate network protocol
* Webmasters can make certain parts off-limits for the crawler by creating robot.txt .

#### 12.6.4.3 Document input stream (DIS)

* Same doc can be processed by multiple processing modules.
* To avoid DL a doc multiple times, we cache the doc using DIS
* DIS cache the entire contents of the doc, cache the small one in memory and larger doc to a backing file.
* Worker thread first extract URL from the frontier, passes the URL to relevant protocol module.
  The protocol module initializes the DIS from a network connection to contain the doc's contents.
  The worker then passes the DIS to all relevant processing modules.

#### 12.6.4.4 Document Dedupe test:

* Many docs on the web are available under multiple different URLs.
* docs are also mirrored on various servers.
* We need to perform a dedupe test on each doc to remove duplication.
* We can calculate a 64-bit checksum and store it in a DB, use MD5 or SHA.

#### 12.6.4.4.1 How big the checksum store?

* Assume 15B and 8-Bytes, then it's 15B * 8-Bytes => 120 GB.
* We can use LRU based cache on each server
* First check cache, then storage, if checksum is found, then ignore the doc. Otherwise
  add to the cache and back storage.

#### 12.6.4.5 URL filters

* We can blacklist some websites.
* We can define filters to restrict URLs by domain, prefix, or protocol type.

#### 12.6.4.6 Domain name resolution.

* We need to map URL to IP address.
* So we need to caching DNS results by building our local DNS server.

#### 12.6.4.7 URL dedupe test

* We will encounter multiple links to the same doc.
* We need URL dedupe test before adding it to the URL frontier.
* We store all the URLs seen by our crawler in a DB.
* We store the checksum.
* We can use cache to store popular URLs.

#### 12.6.4.7.1 How much storage we would need?

* 15B websites * 4-bytes => 60 GB

#### 12.6.4.7.2 User bloom filters for deduping?

* Use a large bit vector
* A doc may incorrectly deemed to be in the set, so it will never be downloaded.
* To reduce the chance, we can make the bit vector larger.

#### 12.6.4.8 Checkpointing

* Regularly write snapshots of its state to the disk. 
* Aborted crawl can be restarted from the last checkpoint.

## 12.7 Fault tolerance

* Consistent hashing for distribution among crawling servers.
* Replacing a dead host and help in distributing load among crawling servers.
* All servers perform regular checkpointing and storing their FIFO queues to disks.
* If a server goes down, we can replace it. And consistent hashing should shift the load to other servers.

## 12.8 Data Partitioning

* We are dealing with 3 kinds of data:
    1. URLs to visit
    2. URL checksums for dedupe
    3. Doc checksums for dedupe
* We are distributing URLs based on hostnames:
    1. Store its set of URLs that need to be visited.
    2. checksums of all the previously visited URLs
    3. checksums of all the downloaded docs.
* Consistent hashing will redistribute the URLs from overloaded hosts
* Each host dump a snapshot of all the data it is holding onto a remote server.
* If a server dies down, another server can replace it by taking its data from the last snapshot.

## 12.9 Crawler Traps

* It causes a crawler to crawl indefinitely. Some are unintentionl, create a cycle.
  Other crawler traps are introduced intentionally.

# Unit 13 Designing Facebook's Newsfeed (NF)

* Facebook's Newsfeed, contain posts, photos, videos and status updates from all the people and pages a user follows.
* Similar Service: Twitter/Instagram/Quora Newsfeed.
* Difficulty: Hard

## 13.1 What is Facebook's newsfeed?

* A Newsfeed is the constantly updating list of stories in the middle of FB homepage.
* Status updates, photos, videos, links, etc.

## 13.2 Requirements and Goals of the System

### 13.2.1 Functional Requirements

* NF will be generated based on the posts from the people, pages, and groups that a user follows.
* A user may have many friends and a large no. of pages/groups.
* Feeds may contain images, videos, or just text.
* Our service should support appending new posts as they arrive to the newsfeed for all active users.

### 13.2.2 Non-Functional Requirements

* Generate user's newsfeed in real-time, max latency would be 2s.
* A post shouldn't take more than 5s to make it to a user's feed assuming a new newsfeed request comes in.

## 13.3 Capacity Estimation

* Assume a user has 300 friends and follows 200 pages.
* Traffic estimates:
    * 300M DAU, each fetch timeline 5 times a day, 1.5B newsfeed requests / day, 17500 requests / sec.
* Storage estimates:
    * 500 posts in every user's feed that we want to keep in memory for a quick fetch.
    * Each post would be 1KB in size.
    * Store 500 KB of data per user.
    * 150 TB memory needed, assume 100 GB memory per server, we need 1500 machines.

## 13.4 System APIs

```python
getUserFeed(api_dev_key, user_id, since_id, count, max_id, exclude_replies)
```

* `api_dev_key`: the API developer key of a registered account. Throttle users based on their allocated quota
* `user_id (number)` : Generate the newsfeed for this user.
* `since_id` (number) : returns results with ID higher than the specified ID, i.e. more recent.
* `count` (number) : specify the number of feed, up to 200 / distinct request.
* `max_id` (number) : The inverse of `since_id`
* `exclude_replies` (boolean) : prevent replies from appearing the returned timeline.

* Return: (JSON) returns a JSON object containing a list of feed items.

## 13.5 DB Design

* Three primary objects: User / Entity (e.g. page, group, etc) / FeedItem (or Post)
* A user can follow other entities and can become friends with other users.
* Both users and entities can post feeditems which contain text, images or videos.
* Each Feeditem will have a UserID pointing to the User who created it.
  For simplicity, we assume that only users can create feed items.
  This is not the case in real facebook.
* Each feeditem can optional have an entityid pointing to the page or the group where that
  post was created.
* Relational DB, we would need to model 2 relations:
    * User-Entity relation, each user can be friends with many people and follow a log of entities.
    * FeedItem-Media relation

* User Table

| PK | UserID: int             |
|----|-------------------------|
|    | Name: varchar(20)       |
|    | Email: varchar(32)      |
|    | DateOfBirth: datetime   |
|    | CreationDate: datetime  |
|    | LastLogin: datetime     |

* Entity Table
    * Type is group / page

| PK | EntityID: int           |
|----|-------------------------|
|    | Name: varchar(20)       |
|    | Type: tinyint           |
|    | Description: varchare(512) |
|    | CreationDate: datetime  |
|    | Category: smallint      |
|    | Phone: varchar(12)      |
|    | Email: varchar(20)      |

* User Follow
    * Type is whether it's a user or an entity

| PK | UserID: int             |
|    | EntityOrFriendID: int   |
|----|-------------------------|
|    | Type: tinyint           |

* FeedItem table

| PK | FeedItemID: int         |
|----|-------------------------|
|    | UserID: int             |
|    | Contents: varchar(256)  |
|    | EntityID: int           |
|    | LocationLatitude: int   |
|    | LocationLongitude: int  |
|    | CreationDate: datetime  |
|    | NumLikes: int           |

* FeedMedia Table

| PK | FeedItemID: int         |
|    | MediaID: int            |
|----|-------------------------|
|    |                         |

* Media

| PK | MediaID: int            |
|----|-------------------------|
|    | Type: tinyint           |
|    | Description: varchare(512) |
|    | Path: varchare(512)     |
|    | LocationLatitude: int   |
|    | LocationLongitude: int  |
|    | CreationDate: datetime  |

## 13.6 High Level System Design

* Divide into 2 parts:

### 13.6.1 Feed Generation

* Newsfeed is generated from the posts of users and entities that a user follows.
* We will perform the following steps:
* Retrieve IDs of all users and entities that Jane follows.
* Retrieve latest, most popular and relevant posts for those IDs.
* Rank these posts based on the relevance.
* Store this feed in the cache and return top posts (say 20) to render.
* On the FE, Jane reaches the end and fetch the next 20 posts.
* If there is new incoming posts from people, we periodically perform above steps to rank
  and add the newer posts to her feed.
* Then Jane can be notified so that she can fetch.

### 13.6.2 Feed publishing

* She has to request and pull feed items from the server.
* When she reaches the end, she can pull more.

### 13.6.3 Components

1. Web servers: maintain a connection with the user.
    * Transfer data between the user and the server.
2. Application server
    * Execute the workflows of storing new posts in the DB servers.
    * APP servers to retrieve and to push the newsfeed to the end user.
3. Metadata DB and Cache: store metadata about Users, Pages and Groups.
4. Posts DB and cache: to store metadata about posts and their contents.
5. Video and photo storage, and cache: Blob storage, store all the media included in the posts.
6. Newsfeed generation service: gather and rank all the relevant posts for a user to
   generate newsfeed and store in the cache. It will also receive live updates and
   will add these newer feed items to any user's timeline.
7. Feed notification service: notify the user that there are newer items available for their newsfeed.

#### 13.6.3.1 Diagram


                                                                                                                 
                                                                                                                                                         
                                                                                                                                                         
                                                                                                                                                          
                                                                                                                                                          
                                                                                                                                                          
                                                                                                                                                          
|--------|  Add/Update Post |------------|                  |-------------------|                        |------------------|                        |-------------|
| User A |<---------------->| Web server |<---------------->| App Server        |----------------------->| Metadata Cache   |<---------------------->| Metadata DB |
|--------|                  |------------|                  |-------------------|                        |------------------|                        |-------------|
                                                                                                         |------------------|                        |-------------|
                                                            |---------------------|                      | Post Cache       |<---------------------->| Post DB     |
                                                            | Newsfeed Generation |--------------------->|------------------|                        |-------------|
                                                            |---------------------|                      |------------------|                        |-------------|
                                                                      |                                  | Media Cache      |<---------------------->| Video/photo |
                                                                      |                                  |------------------|                        |-------------|
                                                                      v
                     |--------------------|                 |-----------------------|
                     | Feed notification  |---------------->| cache servers holding |
		     |--------------------|                 | feed                  |
                                  |                         |-----------------------|
                                  |                                   ^
                                  |                                   |
                                  v                                   v
|--------|  Feed update     |------------|   get feed       |-------------------|
| User B |<---------------->| Web server |----------------->| App Server        |
|--------|                  |------------|                  |-------------------|
                                   ^
|--------|  Feed update            |
| User C |<------------------------|
|--------|                  

## 13.7 Data Partitioning

### 13.7.1 Feed generation

* Issues:
1. A user with lots of friends / follows, the service is slow
2. We generate the timeline when a user loads their page, so this would be quite slow
3. For live updates, each status update will result in feed updates for all followers.
   This could result in high backlogs in our Newsfeed Generation Service.
4. The server pushing newer posts to users could lead to very heavy loads, for people or pages
   that have a log of followers.

* Offline generation for news feed
* Dedicated servers that are continuously generating users' newsfeed and storing them in memory.
* When a user requests for the new posts for their feed, we can simlply serve it from memory.
* When servers need to generate the feed for a user, they will query to see what was the last time the feed is generated.
* New feed data would be generated from that time onwards.

```python
class struct:
    def __init__(self):
        self.feedItems = # <FeedItemID, FeedItem>
```

* When a user want to fetch more feed items, they send the last feeditemID they currently see,
* Then we jump to that FeedItemID in the hash map and return next batch/page from there.


## 13.9 Data Partitioning

# Q&A

Q: In 2.6.1, Why we don't need store this sequence number?
A: Is it because in the 2.6.2 diagram, it will keep looping steps 3 ~ 6, until the encoded URL is new.

Q: In 2.6.3, single point failure. How the standby take over?
A: Assume the not used keys and the used keys are stored in disk, and the disk doesn't die.
   Then it makes sense. Otherwise, if the disk also died, seems not be able to recover

Q: In 2.7, it doesn't actually cover data replication.

Q: In 4, I am still feel confused about sharding.

Q: In 5.6.2 didn't go into Metadata DB deeply

Q: In 5, looks like I am not clear about the flow. I need to use an example to go through the flow
A: In 5.7, it has a flow.

Q: 5.8.2 In-line deduplication doesn't give any benefits for BW.

Q: 5.8.11 How LB work with data partition?

Q: 6.5.2 when use Hbase, what is the key

Q: 6.10.2 what is manufacturer server?

Q: 8.7.1 what is HDFS and GlusterFS and Bigtable?

Q: 8.9 Don't we have to wait for the video upload finish to know if there is duplication?

Q: 8.12 I don't quite understand CDN

Q: 9.3 Why we need to traverse back using the parent reference?

Q: 9.6.2 Even we partition based on range, what if the query on a server go beyond the range, i.e. AABB, AABBB, AABBBB

Q: 10.8.1 what is Redis?

Q: 12.6.4.2 What is the robot.txt

Q: 12.6.4.5 Although checksum is same, looks like we still have to download all doc?
