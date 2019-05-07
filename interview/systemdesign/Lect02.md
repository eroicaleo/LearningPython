
# Useful links

* 专栏 -》 系统设计
* 数据库具体如何建index查询：“B+ tree”
* mini casasandra in lintcode: http://www.lintcode.com/problem/mini-cassandra/
* www.jiuzhang.com/qa/

# Slide 2 课程大纲

* Design User System
    * Memcached, how to use it to optimize DB access.
    * Authentication, 如何保持用户登陆状态。
    * SQL vs NoSQL
    * Friendship, 存储用户好友关系。
* How to scale?
    * Sharding
    * Consistent Hashing (lecture 5)
    * Replica (lecture 5)
* 系统设计不想算法，只要做过类似的，差不多的都能答。

# 3 Design User System

* 设计用户系统，实现功能包括：注册，登陆，用户信息查询，好友关系存储。

# 4 4S - Scenario, Service, Storage, Scale

* Scenario
    * 注册，登陆，查询，用户信息修改
    * 哪个需求量大？查询：一登陆/一刷新/就查询。
    * 支持100M DAU
    * 注册，登陆，信息修改QPS约
        * 100M * 0.1 / 86400 ～ 100
        * 0.1 = 平均每个用户每天登陆+注册+信息修改
        * Peak = 100 * 3 = 300，倍数2-9都合理
    * 查询的QPS约
        * 100M * 100 / 86400 ～ 100k
        * 100 = 平均每个用户每天与查询用户信息相关的操作次数（查看好友，发信息，更新消息主页）
        * peak = 100k * 3 = 300k, SQL ~ 1k QPS, Memcached ~ 1M QPS, if use mysql,
          then needs 300 ~ 600 machines.
        * We have to analysis QPS first. TinyURL 看似QPS很高，分析了之后发现不高。
* Service服务，大事化小。
    * 一个AuthService负责登陆注册
    * 一个UserService负责用户信息存储与查询
    * 一个FriendshipService负责好友关系存储

# 4S - Storage: QPS与常用数据存储系统

* MySQL / PosgreSQL: SQL数据库 ~ 1k QPS这个级别。
* MongoDB / Cassandra: 硬盘型NoSQL数据库 ~ 10k QPS
* Redis / Memcached: 内存NoSQL数据库 ～ 100k - 1m QPS
* NoSQL 最初诞生是为了记log，什么事情什么时候发生。

* 注册，登陆，信息修改，300QPS，适合什么数据系统？MySQL就可以
* 用户信息查询，如果MySQL 300 ～ 500台，Cassandra 30 ~ 50台，Memcached 3 ~ 5台
* memcached 非持久化数据存储，但是效率高。

# 7 用户系统特点

* 读非常多，写非常少。
* 一个读多写少的系统，一定要使用cache进行优化。发生改变的可能性很低。
* How about web crawler 爬虫系统 eg. google？写多读少，从google的角度来说。
* 给人用的系统，读多写少。给机器用，读少写多。

# 8 Storage: Cache

* Cache 是什么？
    * 缓存，把之后可能要查询的东西先存一下。下次要的时候，直接拿。无需重新计算。
    * 可以理解成一个java中的hashmap。
    * key-value的结构。
* 常用的cache系统/软件？
    * Memcached(不支持数据持久化)
    * Redis(支持数据持久化)
* Cache一定在内存中吗？
    * 是个概念，不限定存储介质。
    * CPU cache 是memory 的cache
    * memory 是File system 的cache.
    * File system 是 网络的cache，就像google，把网页存在硬盘上。
    * 对于复杂计算，也可以把结果先存在file system上。记忆化搜索。
* Cache 一定在server cache 吗？
    * 不一定，Frontend/Client/Browser也可以有客户端的cache。
    * 第二次加载网页，从本地加载图片，网页变快。

# 10 Memcached

* 一款负责帮你cache在内存里的软件，非常广泛使用的数据存储系统。

# 11 Memcached 使用例子

```python
cache.set("this is a key", "this is a value")
cache.get("this is a key")

cache.set("foo", 1, ttl=60) # ttl is time out
cache.get("foo")

# wait for 60 seconds
cache.get("foo")

cache.set('bar', 2)
cache.get('bar') # 2

# 'bar' maybe evicted by cache, if memory is full.
cache.get('bar')
```

* Cache 淘汰算法
* LRU (Least Recent Used Cache)
* LFU 给了参考论文，LRU 被问烂了。

# 12 Memcached 如何优化DB的查询

```python
class UserService:
  def getUser(self, user_id):
    key = 'user::%s' % user_id
    user = cache.get(key)
    if user:
      return user
    user = database.get(user_id)
    cache.set(key, user)
    return user

  def setUser(self, user):
    key = 'user::%s' % user.id
    cache.delete(key)
    database.set(user)
```

# 13 哪种写法对？

```python
A. database.set(user); cache.set(key, user);
B. cache.set(key, user); database.set(user);
C. cache.delete(key); database.set(user);
D. database.set(user); cache.delete(key);
```

* 在任何时候，第一句话或者第二句话都可能挂掉，返回error。
* A第一句话挂了，没有问题，`setUser` 结束。database cache are consistent.
* A第一句成功，第二句话挂了。 database has new data, cache has new data, inconsistent.
  Future reading will most like to get dirty data.
* B same reason.
* C is safe.就算第二句失败，cache里也没数据。要保证db is source of truth.
* D same as A B, cache will have dirty data.

* Nice to have/understand
    * 即使C也有可能出问题，如果`user = database.get(user_id)` 和 `cache.set(key, user)`
      另外一个进程插入了`setUser`, 那么cache里又变成了dirty data.
    * 但是这样的情况概率很小。一般只有用户自己修改信息，用户同时get/set不太可能。
    * 无论如何优化，都可能因为并发性，出现inconsistent。用timeout一天之后自动失效。
      专业术语：eventually consistent

# 15 Authentication Service

* 用户是如何实现登陆与保持登陆的？如何识别下次登陆不需要输入密码
* 服务器端如何创建session table。

| Header One     | Header Two     | Header Two     |
| :------------- | :------------- | :------------- |
| session_key    | string         | 一个hash值，全局唯一，无规律 |
| user_id        | Foreign key    | 指向User Table |
| expire_at      | timestamp      | 什么时候过期 |

* 用户登陆流程：
    * 用户登陆：系统创建session key
    * 把session key作为cookie值返回给浏览器
        * cookie相当于一个badge
    * 浏览器将该值记录在浏览器的cookie中
    * 用户每次向服务器发送的访问，自动带上该网站所有的cookie
        * 所以只把必须的信息放在cookie里
    * 此时服务器检查到cookie中的session key有效，认为用户登陆了。
        * 如果session key泄露，别人就可以登陆
* 用户logout之后
    * 从session table里删除对应数据
* 问题：session table 存在哪儿？
    * A：数据库
    * B：缓存
    * C：都可以
    * 解答：理论上都可以。
    * 如果小网站，可以用缓存/cache，因为断电了没关系。
    * 如果是大网站facebook：只存在缓存中，虽然不会out of memory,
      session table is really small。一旦挂机，一大波用户同时来登陆。系统就是写多读少。
      所以大网站存在数据库中保险。如果访问多，可以用cache优化。因为用户发任何request都会
      查询session key。

# 17 小结

* 对于user system而言，写很少，读很多
* 写操作少，从QPS的角度说，一台SQL就可以了
* 读操作多，可以用memcached进行读操作优化。
* 如果读写操作都很多，怎么办？
    * 方法一：使用更多数据库服务器分摊流量
    * 方法二：使用像redis这样的读写操作都很快的cache through型DB
        * memcached 是一个cache-aside的DB，client需要自己负责管理cache-miss时数据的loading。
        * Redis又有数据持久化的能力。
        * Cache和数据库的打包，memory和disk的打包。

# 18 Cache aside

* 服务器(web sever)分别与DB和Cache进行沟通。
    * slide 12 的程序就跑在web server上。它是DB和cache的client。
* DB和Cache之间不直接沟通。
* 业界代表：Memcached + MySQL

# 19 Cache through

* 服务器(web sever)只和打包好的Cache进行沟通。
* Cache负责和DB去沟通，把数据持久化。
* 业界代表：Redis，它包含了一个cache和一个db。
* 业界更多选择memcached，稳定性更高，更易扩展。

# 22 Friendship Service

* 单向好友关系（Twitter, Instagram, 微博）
    * 就是一条有向边

| Friendship Table | Header Two     | Header Two     |
| :------------- | :------------- | :------------- |
| from_user_id   | Foreign key    | 用户主体        |
| to_user_id     | Foreign key    | 被关注的人        |

* 双向好友关系 （Whatsapp, Facebook, 微信）
    * 方案1: 存为两条信息，A关注B, B关注A。
    * 方案2: 存为一条信息，id小的在前，id大的在后。

* 好友关系操作非常简单，基本都是key-value
    * 某个user的所有关注对象
    * 某个user的所有粉丝
    * A关注B, 就插入一条数据
    * B关注A, 删除一条数据。

* User table 需要存用户名，密码等，query方式复杂。有可能按照email/phone number/id去查询。
  所以大部分网站不选择NoSQL数据库。

# 23 SQL vs NoSQL

* Friendship Table 适合什么数据库？
* SQL和NoSQL的选择标准。

# 24 数据库选择原则1

* 大部分情况，SQL/NoSQL都可以。
* System Design很少有只能选这个，不能选那个。

# 25 数据库选择原则2

* 需要支持Transaction的话不能选NoSQL。
* Transaction: 像是银行交易。发红包，A的钱发给了B。

``` python
A.money -= 10
B.money += 10
# 必须同时成功活着失败的另一个例子
database.set(user); cache.delete(key)
# 无法做transaction: 1. 不是同一款软件。2. 不在同一台机器上。
```

* 必须同时成功活着失败。

# 26 数据库选择原则3

* 想不想偷懒
* SQL帮忙做很多事情：
    * serialization, email/password/full name/ 数据类型全都不一样。存到硬盘上全都是
      字符串。
    * secondary index
* NoSQL

# 28 Friendship Service

* 如果存在SQL

| Friendship Table | Header Two     | Header Two     |
| :------------- | :------------- | :------------- |
| smaller_user_id   | Foreign key    | 双向好友关系中id小一点的，index=true    |
| bigger_user_id     | Foreign key    | 双向好友关系中id大一点的，index=true   |

* 查询好友关系时
    * 给定的user id
    * select bigger_user_id from friendship where smaller_user_id = user_id
    * select smaller_user_id from friendship where bigger_user_id = user_id

* 如果存在nosql
* 很多nosql不支持multi indexes
* 查分两台数据
    * A的好友B: key = A, value = B
    * B的好友A: key = B, value = A

# 29 例子

* 好友关系存一份
* 查询2的好友：select from friendship where bigger_user_id = 2 or smaller_user_id = 2

| smaller_user_id | bigger_user_id     |
| :------------- | :------------- |
| 1       | 2       |
| 1       | 3       |
| 2       | 3       |

* 好友关系存两份
* 查询2的好友：select from friendship where from_user_id = 2

| from_user_id | to_user_id |
| :----------: | :--------: |
| 1       | 2       |
| 2       | 1       |
| 1       | 3       |
| 3       | 1       |
| 2       | 3       |
| 3       | 2       |

* 效率没有多大差别，第二种稍微快一点。
* 数据库会对每一个column帮助建index，如果不建index，就要做for loop。
* 具体如何建index查询：“B+ tree”

# 30 以 Cassandra 为例剖析典型的NoSQL数据结构

* Cassandra是一个三层结构的NoSQL数据库，又叫三元组结构。
    * http://www.lintcode.com/problem/mini-cassandra/
    * 新企业用的很多用NoSQL
    * Facebook用的是它们自己开发的graphDB.
* 第一层：row_key
    * 又称为hash_key
        * Cassandra最有用的地方就是分布式数据库系统
        * 我们要知道一个数据分布在哪里。
        * row key 决定了他在哪台机器上。
    * 也就是我们传统所说的key-value中的那个key
    * 任何查询都要带上这个key，无法进行range query
        * 因为做了hash，没有办法查询user 1 - 100
    * 最常用的row_key：user_id
* 第二层：column_key
    * 是排序的，可以进行range query。没有做个hash。
        * 可以这样，user id = 1, column key = [200,300]
    * 可以是复合值，不如是一个timestamp + user_id的组合。
* 第三层: value
    * 一般来说是String。
    * 如果需要存很多信息的话，可以自己做 serialization。
    * serialization: 把一个object / hash 序列化为一个string，比如把一个二叉树序列化。

```java
public void insert(String row_key, int column_key, String column_val) {
}

public List<Column> query(String row_key,
                          Integer column_start,
                          Integer column_end) {

}
```

# 33 SQL VS NoSQL

* SQL的column是在Schema中预先指定好的，不能随意添加。
* 一条数据一般以row为单位（取出整个row作为一条数据），所以又叫行式存储。

| SQL | id | username | email | password | first name | ... |
| :-- | :- | :------- | :---- | :------- | :--------- | :-- |
| Row1|    |          |       |          |            |     |
| Row2|    |          |       |          |            |     |

* NoSQL 的column是动态的，无限大，可以随意添加。可以叫列式存储
* 一条数据一般以grid为单位：row_key + column_key + val = 一条数据。
    * 以行号+列号定位到一个数据。
* 只需要提前定义好column_key本身的格式(是一个int还是一个int+string)
* row key可能是id，column key可能是username，剩下的打包放在一个grid里。压缩起来，serialization。
* 局限是不能用value里的值进行query，比如不能用email。
* 但是效率可能更高。

| NoSQL | col1 | col2 | col3 | col4 | col5 | ... |
| :-- | :- | :------- | :---- | :------- | :--------- | :-- |
| Row1| val0 | val1   |       |          |            |     |
| Row2|      |        |       |          |            |     |

* 如何把friendship table 存在 Cassandra NoSQL 里
    * 怎么存依赖你有什么样的需求，需求不同，存法不一样。
    * 需求1: 查询A-B是不是好友。一个同学提出row key = user id, column key = # of friends
      好友作为list存在val里。但是这样就没法简单的查询A-B是不是好友。
    * 比较合理的做法row key = user id， col key = other user id, val = whatever you
      want: [is mutual friend, is blocked, timestamp]
    * 如果要查询A的所有好友，指定row key = A，不指定col key
    * 如果要查询A-B是不是好友，row key = A，col key start / end = B.

# Cassandra 存储 NewsFeed

* Slide 34 News Feed Table
* 我们需要怎样的查询？
    * 需求1：查询一个用户的所有tweet，所以user id 肯定要作为一个 row key。
    * 接下来看前多少条，就要把tweet按时间倒序排列，所以column key = <created_at, tweet_id1>
    * val 就可以是tweet data.

# Cassandra 例子和总结

* Cassandra为代表的NoSQL存储数据相当于一个一个的三元组，比如存储好友关系时：
    * 1-2 好友
    * 2-3 好友

| row_key | column_key | value |
| :-----: | :--------: | :---: |
| 1 | 2 | null |
| 2 | 1 | null |
| 2 | 3 | null |
| 3 | 2 | null |

# 38 Interviewer: How to scale?

* 系统设计的日经题
* last step in 4S: Scenario/Service/Storage/Scale

# 39 除了QPS，还有什么需要考虑的？

* 100M的用户存在一台MySQL数据库里也存的下，storage没问题
* cache优化读操作后，300QPS的写，QPS也没问题。
* 还有什么问题？

# 40 单点失效 single point failure

* 万一这一台数据库挂了
* 短暂：网站不可用
* 彻底：数据全丢失
* 不能把所有的鸡蛋放在一个篮子里

# 41 两件事

* Sharding:
    * NoSQL 把数据存在不同的机器上
* Replica

# 42 Sharding / Replica

* 数据拆分 Sharding，row kew/sharding kew/hash key/partition key 是同一个意思。
    * 按照一定的规则，将数据拆分成不同的部分，保存在不同的机器上。
    * 就算挂一台，网站也不会100%不可用。
* 数据备份Replica
    * 通常的做法是一式三份（重要的事情写三遍）。三份同时不能访问概率极低。
    * Replica 同时还能分摊读请求。

# 43 Sharding in SQL vs NoSQL

* SQL 自身不带Sharding功能，需要码农亲自上手。
* Cassandra为例的NoSQL大多数都自带Sharding，码农可以偷懒。
* 它们的做法都是一样的。

# 44 数据拆分 Sharding

* vector sharding
* horizontal sharding

# 45 纵向切分

* User table 一台数据库
* Friendship table 一台
* Message Table 一台

# 46 复杂一点的vertical sharding

* User table包含：Email/Username/Password/push_preference/avatar
* email/username/password 变动较小
* push reference, avatar变动频率高
* 拆分成两个table，user table + user profile table 放在两个机器上。user profile table
  挂了仍然可以登陆。
* Vertical sharding的缺点是什么？不能解决什么问题？
    * 依然存在single point failure

# 47 横向拆分

* 核心考点

# 48 粗暴想法

* Friendship table
* 有10台数据库机器
* 按照from_user_id % 10进行拆分，问题是啥？
    * 每台机器分配到的不均匀，这个问题还不算严重。

# 49 加机器怎么办？

* % 10 变成 % 11 所有数据都要大迁移。

# 50 过多数据迁移会造成的问题：

* 慢，牵一发动全身
* 迁移期间，服务器压力增大，容易挂
* 容易造成数据不一致性。

# 51 怎么办

* 一致性Hash算法 consistent hashing

# 52 Consistent Hashing

* why do we need it?
    * % n is the simplest hash algorithm
    * when n -> n+1, key % n and key % (n+1) most likely will be different
    * it's not Consistent Hashing

# 53 Consistent Hashing

* one simple Consistent Hashing
    * key模一个很大的数，比如360
    * 360分配给n台机器，每个机器负责一段区间
    * 区间分配记录在一张表，存在web server上。
    * 新加一台机器的时候，在表中选择一个位置，匀走相邻两台机器的一部分数据
        * 不是变化他模多少
* 比如n 从2变到3，只有1/3的数据移动。
    * 比起52页75%的数据好多了。
    * In general, 1/(n) -> 1/(n+1), only 1/(n+1) data needs to be move.
    * This is just basic idea, in reality, there are more details and tricks.

# Q&A

* 什么是push preference?
    * 发生什么样的情况给发push。比如谁发帖要提醒，加好友要不要提醒。
* LFU 和 LRU 都用在什么情况？
    * LRU 更加常用。
* 问答板块提问。
    * www.jiuzhang.com/qa/
