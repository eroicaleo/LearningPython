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
