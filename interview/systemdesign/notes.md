# Lecture 1: Introducing system design & news feed system

## slide 1

* System Design/OO Design/API Design
* Need to check with HR, which kind of design will be in interview
* System design: high level
* OO/API Design: the interaction between classes.
* API Design questions: web technology
    * how dose mobile/web interaction
    * Given a class, define the interfaces and methods
    * Have to have project experiences, otherwise no feeling about why this design is good
      another design is bad
* The knowledge in this system design course is closely related to web technology.
    * web technology will always be needed
* System design: architecture/infrastructure
    * Covering database/website/mem-cache, how they work together to make a product
    * Today's topic news feed system: facebook/twitter/RSS

## slide 7

* System Design interview two forms:
    * Design Twitter/Facebook/Uber/Whatsapp/Yelp/Tiny URL/NoSQL
    * Trouble Shooting: what happened if we cannot access a website/webserver is too slow/for increasing traffic
* Couple years ago, how to design a whole system
* Nowadays, how to design a specific feature in the whole system

## slide 8

* Design a twitter/design a twitter feature

## slide 9

* Wrong solution #1: listing keyword: load balancer/MongoDB/...
* Veteran programmer, analyze what to do, step by step.
    * Start from a few users, maybe just 2. No need for anything fancy.
    * System with 2/200/2M/200M is all different

## slide 10

* Work Solution 25%, can it work for at least 2 users?
* Special Case 20%
* Analysis
* Tradeoff
* Knowledge Base

## slide 11 4S method

* Scenario, Service, Storage, Scale
* Scenario: ask interviewer questions
    * What functions? Twitter has so many functions, no time to design them all in interview.
    * What features?
    * QPS Query per second
    * DAU daily active users? Design for how many people? 1/2/100M?
* Service:
    * Is it just a small feature
    * Or a big application: how to split big application into small modules,
      a really important sign for engineering ability
    * How service interacts with each other?
    * A good engineer deal a small problem one at a time
* Storage:
    * Schema/DATA/SQL/NoSQL/File System
    * popular area for questions
    * How you store decides how you access
    * Schema: what info to store, for twitter, no need for height and weight, but for medical app
      this is important.
    * Very close to OO design
* Scale:
    * Sharing/Optimize/Special case
    * When user grows, machine down, how to recover

## slide 13 Scenario

* Ask/Analysis

## slide 14 Scenario - Ask

* Ask interviewer
* What functions
* DAU 150M / MAU 313M: DAU is useful for comupting QPS

## slide 15 Scenario - what features

* Step 1: Enumerate all features
    * register / login
    * User profile display / edit
    * Upload image / video
    * Search
    * Post / share a tweet
    * Timeline / News Feed
    * Follow / Unfollow a user
* Step 2: Sort, choose the core functions, don't have enough time
    * Post / share a tweet
    * Timeline / News Feed
    * Follow / Unfollow a user
    * register / login

## slide 16 Scenario - Analysis & Predict

* Concurrent User
    * Average QPS ~ 100k
    * peak QPS ~ 3 * Average = 300k
    * Fast Growing Peak users * 2
* Read QPS: 300k
* Write QPS: 5k

## slide 17 How to use QPS

* QPS = 100, laptop is good enough for webserver
* QPS = 1k
    * needs a good desktop
    * needs to consider single point failure, server is doing sth. really slow.
* QPS = 1M
    * needs to have 1000 cluster
    * What if some of them are down
* QPS and Web Server / DB
    * One web server is about 1k QPS, just the ballpark estimation, some queries
      are slow, some are fast.
        * AJAX or Apache tests are static, no DB access, so can be as high as 10k
        * Not realistic in real industrial applications.
    * The performance is also bounded by performance of DB.
    * SQL ~ 1k QPS, Cassandra ~ 10k, Memcached ~ 1M QPS

## slide 18 Service

* Split big system into small services.
    * Replay 重放需求
    * Merge 归并需求

## slide 19 Service: big system into small service

* User Service
    * Register
    * Login
* Tweet Service
    * Post a tweet
    * News Feed
    * Timeline
* Media Service
    * Upload Image
    * Upload Video
* Friendship Service
    * Follow
    * Unfollow

## slide 20 Service: big system into small service

* Step 1: Replay, replay each request, adding one service for each request
* Step 2: Merge, merge similar service
* What is service: processing similar request

## slide 21 Storage

* The most important part, have the biggest weight. Scenario/Service 10%
  Scale 10%, Storage 50%.
* How to store/access the data.
* 为每一个Service选择存储结构
* Schema细化表结构

## slide 22 data store and access

* 3 places to store data:
    * memory, for DATA which is OK to loose after shut down, Memcached.
    * structured data, e.g. a user's basic info: username/password/email/when
      to log on, better to store in DB, SQL/NoSQL.
        * structured data is like a class, contains some attributes.
    * File system, e.g. Amazon S3, good for non structured data, like images
      videos, media files.
        * Just a sequence of binary bit.
* 关系型数据库SQL Database
    * User Table
* 非关系型数据库NoSQL Database
    * Tweets
    * Social Graph (followers)

## slide 23 Storage data store and access

* Step1: Select
    * For each application and service, choose appropriate structure.
        * structured data -> DB
        * Non structured data -> Filesystem
        * OK to lost -> Memory
* Step2: Schema
    * 细化数据表结构

| Service Type   | Storage Type   |
| :------------- | :------------- |
| User Service   | SQL            |
| Tweet Service  | NoSQL          |
| Media Service  | Filesystem     |
| Friendship Service  | SQL/NoSQL |


* Program = Algorithm + Data Structure
* System  = Service + Data Storage

## slide 25 Storage data store and access, Schema what attributes to store

* User Service

| User Table |      |
| :------------- | :------------- |
| id      | integer       |
| username      | varchar       |
| email      | varchar       |
| password      | varchar       |

* Friendship Table

| Friendship Table |      |
| :------------- | :------------- |
| from_user_id | Foreign Key      |
| to_user_id      | Foreign Key   |

* Tweet Service

| Tweet Table |      |
| :------------- | :------------- |
| id | integer      |
| user_id      | Foreign Key   |
| content      | text   |
| created_time | timestamp   |

* Media Service, not structured data, so no attributes.

## slide 28 新鲜事系统 News Feed

* What is News Feed?
    * After you log on to Facebook/Twitter/朋友圈 之后看到的信息流。
    * All the new messages from your friends.
    * Timeline: the moments that each user you follow posted
    * News Feed: combine all the time line together.
* Typical news feed system
    * Facebook
    * Twitter
    * 朋友圈
    * RSS Reader/今日头条
* 新鲜事系统的核心因素
    * 关注与被关注
    * 每个人看到的新鲜事都是不同的

## slide 29 Storage - Pull Model

* 算法
    * When the user check the news feed, get the first 100 tweets from friends
      and combine them, get the first 100 news feed
    * Merge K Sorted Arrays
* 复杂度分析
    * News Feed, Assume following N friends, then needs to read DB N times +
      Merge K Sorted Arrays (negligible).
        * Why K-way merging can be ignored? It's doing in memory. DB reads is
          way slower, 1000X or 1MX
        * DB access is ~ milliseconds, arithmetic operations ~ nanoseconds
        * DB access can be lightweight or complex access.
    * Post Tweet => 1 DB writes

## slide 29 Storage - Pull Mechanism

1. User send request to get News Feed
2. Web Server get followings from "Friendship Table"
3. Web Server get tweets from followings from "Tweet Table"
4. Merge and return to User

## slide 30 Pull model's 缺陷

```python
def getNewsFeed(request):
    followings = DB.getFollowing(user=request.user)
    news_feed = empty
    # N reads is really slow
    # And it's serial, blocking
    for follow in followings:
        tweets = DB.getTweets(follow.to_user, 100)
        news_feed.merge(tweets)
    # Don't even need to do K-way merging, since it's not bottleneck
    sort(news_feed)
    return news_feed

def postTweet(request, tweet):
    DB.insertTweet(request.user, tweet)
    return success
```

## slide 33 Storage - Push Model

* Algorithm:
    * Create one list for each user's news feed
    * User post a tweet, this tweet will be pushed to other user's news feed
      list, it's called fanout, more useful to mention in interview.
    * When user checks news feed, just need to get the most recent 100
* Complexity analysis
    * News Feed => Just needs 1 DB read
    * Post a tweet => N 粉丝，N DN writes
        * Writes are slower than reads
        * Celebrity can have huge number of fans
    * Good part: can be done async in the background, no user waiting time.

| News Feed Table |    |
| :------------- | :------------- |
| id       | integer       |
| owner_id | Foreign Key       |
| tweet_id | Foreign Key       |
| created_at | timestamp       |

## slide 34 News Feed Table

| id     | owner id     | tweet id     | created at     |
| :------------- | :------------- | :------------- | :------------- |
| 1      | 东邪       | 东邪：好想念超风 | 16:30 |
| 2      | 西毒       | 东邪：好想念超风 | 16:30 |
| 3      | 西毒       | 西毒：好想念嫂子 | 16:35 |
| 4      | 郭靖       | 郭靖：华筝怎么样 | 17:00 |
| 5      | 东邪       | 郭靖：华筝怎么样 | 17:00 |
| 6      | 西毒       | 郭靖：华筝怎么样 | 17:00 |
| 7      | 黄蓉       | 郭靖：华筝怎么样 | 17:00 |
| 8      | 黄蓉       | 黄蓉：男人不东西 | 18:00 |
| 9      | 郭靖       | 黄蓉：男人不东西 | 18:00 |
| 10     | 东邪       | 黄蓉：男人不东西 | 18:00 |

* 通过一句sql语句就可以拿到:
    * `select from news_feed_table where owner_id = 黄蓉 order_by created_at desc limit = 20`

## slide 35 Storage - Push 原理图

* 1. Post a new tweet
* 2. Web Sever insert the tweet to DB
* 3. Web Sever send tweets web message queue, the Async Tasks Server.
* 4. ATS get followers
* 5. ATS fanout: insert new tweet to followers news feed

## Slide 36 drawbacks of Push model

* Some one said it's wasting DB, disk space.
    * Disk is cheap, no need to worry.
* Fanout can be slow because followers can be huge.

## Slide 37 Storage - Push Model

```python
def getNewsFeed(request):
  return DB.getNewsFeed(request.user)

def postTweet(request, tweet_info):
  tweet = DB.insertTweet(request.user, tweet_info)
  AsyncService.fanoutTweet(request.user, tweet) # Async execution
  return success

def fanoutTweet(user, tweet):
  followers = DB.getFollowers(user)
  for follower in followers: # followers can be a huge list, 10M
    DB.insertNewsFeed(tweet, follower)
```

## Slide 38 Pull vs Push

## Slide 39 Storage Pull vs Push

* Popular Social App
    * Facebook - Pull
    * Instagram - Push + Pull
    * Twitter - Pull
    * Why most companies choose Pull model?
        1. Push has big delay.
        2. 僵尸粉
* 误区
    * 不坚定想法，摇摆不定。
    * 不能表现出Tradeoff的能力。
        * Need to show tradeoff ability, can we improve drawbacks? Is it easy?
    * 无法解决特定问题。

## Slide 40 4S

* 已经得到一个可行方案
* Scenario场景
    * 和面试官讨论
    * 搞清楚需要设计哪些功能
    * 并分析出所设计的系统大概需要支持的Concurrent Users/QPS/Memory/Storage
* Service服务
    * 合并需要设计功能，相似的功能整合为一个Service
* Storage存储
    * 对每个Service选择合适的存储结构
    * 细化数据表单
    * 画图展示数据存储和读取的流程
* 得到一个Work Solution而不是Perfect Solution
* 这个Work Solution可以存在很多要解决的缺陷

## Slide 41 Scale扩展

* How to scale?系统如何优化与维护
1. optimize
2. Maintenance

## Slide 42 扩展-如何优化系统

* Step 1: Optimize
    * Solve Problems/Limitations
        * Pull vs Push, Normalize vs De-normalize
    * More features
        * Edit, Delete, Media, Ads
    * Special Cases
        * Lady Gaga, Inactive Users
* Step 2: Maintenance
    * Robust
        * What if one server/DB is
    * Scalability
        * 流量暴增，如何扩展

## Slide 43 Scale - 解决Pull的缺陷

* 最慢的部分发生在用户读请求时（需要耗费用户等待时间）
    * 在DB访问之前加入Cache
    * Cache每个用户的Timeline
        * N次DB请求 -》 N次Cache请求（N是关注的好友个数）
        * Trade off Cache所有的？Or Cache the most recent 1000
        * Twitter has 300M user, cache 100 per user, 30B messages = 30G messages
          1kB per message, = 30TB memory
        * Twitter/Facebook has millions of machines.
        * N times DB read becomes N times memory read, 1000X speed up
    * Cache每个用户的News Feed (Slide 34)
        * 没有Cache News Feed的用户：归并N个用户最近的100条Tweets,然后取出结果的前100条
        * 有Cache News Feed的用户： 归并N个用户在某个时间戳之后的所用Tweets。
        * It's OK to loose them in cache, just need to rebuild them.

## Slide 44 Scale - 解决Push的缺陷

* 浪费更多的存储空间Disk
    * 与Pull模型将News Feed存在Memory中相比，Push将News Feed存在Disk里完全不是个事儿
    * Disk is cheap
* 不活跃用户
    * 没有太好办法，rank followers by weight (e.g. last login time)
* 粉丝数目 >> 关注数目
    * Like lady gaga
    * 无解？完全切换回Pull?
    * Trade off: Pull+Push vs Pull

## Slide 45 Scale 扩展 - Lady Gaga

* Lady gaga 65.5M
* Push model's challenge: fanout needs hours.
* Wrong answer in interview: "Push has problems, switch to pull."
* Correct answer
    * 尝试现有模型下做最小的改动来优化，比如多加几台机器。新年期间，新帖特别多。不用改代码。
    * 对长期的增长进行估计，评估是否值得转换模型。
    * A lot of social app use push model at first, but eventually switch to pull
      model.
    * Because push is easy to implement and pull model is bug prone/hard to implement
      /needs more memory.

## Slide 46 Scale 扩展 - Lady Gaga

* Push + Pull optimization
    * normal user (e.g. < 1M followers) 仍然用push
    * Lady gaga, Celebrity, don't push to user's news feed
    * 用户需要时，来明星的Timeline里取，合并到News feed里。（push do sth/pull do sth）。
* 摇摆问题
    * 明星定义，用户关注/取关，不影响是不是明星。
    * 邓超掉粉
    * 解决方法
        * 明星用户发Tweet后，依然继续Push 他们的Tweet到所有用户的News Feed里，原来的代码
          就不用改了
        * 将关注对象中的明星用户的timeline与自己的newsfeed进行合并后展示
            * 但并不存储进自己的news feed列表里，push来做这个事。

## Slide 48 Scale 扩展 - Pull vs Push

* Everybody uses pull, why we need to learn push
    * system design doesn't choose the best solution
    * 选择一个最合适的方案
    * 没有大流量，push是最经济最省力的做法
* 系统设计面试并不是期望答出最优的解决方案，从分析中判断你对系统的理解和知识储备。

| when push? | when pull?     |
| :------------- | :------------- |
| 资源少       | 资源充足       |
| 少写代码       | Item Two       |
| 实时性要求不高 | 实时性要求高       |
| 用户发帖比较少       | 用户发帖多       |
| 双向好友关系，没有明星问题 （微信朋友圈）| 单向好友关系，明星问题       |

* 东邪老师认为朋友圈用的是push模型
