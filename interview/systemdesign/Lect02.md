
# Useful links

* 专栏 -》 系统设计

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
