
# Useful links

http://www.lintcode.com/problem/consistent-hashing
http://www.lintcode.com/problem/consistent-hashing-ii
http://www.juzhang.com/qa/2067
http://www.lintcode.com/problem/tiny-url
http://www.lintcode.com/problem/tiny-url-ii



# Slide 3 课程大纲

* Consistent Hashing
    * 简单的Consistent Hashing方法回顾及缺陷分析。
    * 一个更优的Consistent Hashing方法。
* Replica
    * SQL 通常如何进行备份。
    * NoSQL 通常如何进行备份。
* 设计一个短网址系统 Design tiny url
    * 高频题 > 30%
    * 4s 分析法。
    * No hire/weak hire/hire/strong hire.
* 附录：
    * 当你访问`google.com`时发生了什么事？

# Slide 4 一致性哈希算法 Consistent Hashing

* Vertical Sharding/partition
    * User table一台机器，friendship table 一台机器。一个人一百个好友
      friendship table 就是 user table 的 100 倍。
* Horizontal Sharding/partition
    * 尽量把数据平摊在机器上，也就分摊了读写的压力。
    * 所以 vertical sharding 不好，因为不平均。

# Slide 5 Consistent Hashing

* 为什么需要一致性哈希
    * % n 是最简单的 hash 算法
    * n 变 n+1 时，key % n and key % (n+1) 一般都不一样。
    * 这就叫不一致哈希。
    * 12 个数据，3台机器变成4台机器，75%的数据都会迁移。
* 数据迁移导致什么问题？
    * latency变大，因为机器要忙着迁移，没有时间响应用户需求。
    * inconsistency，迁移和数据更新顺序不对，导致不一致。

# Slide 6 Consistent Hashing

* one simple Consistent Hashing
    * key模一个很大的数，比如360
    * 360分配给n台机器，每个机器负责一段区间
    * 区间分配记录在一张表，存在web server上。
    * 新加一台机器的时候，在表中选择一个位置，匀走相邻两台机器的一部分数据
        * 不是变化他模多少
* 比如n 从2变到3，只有1/3的数据移动。
* 再考虑3台到4台的变化，有了A/B/C，新来了D，应该如何分配数据？
    * 找两台连续的机器，看哪两台覆盖的数据最大，把他俩三等分。移动的数据只有22%。

# Slide 8 Consistent Hashing

* 每次加一台机器，只有一台或两台数据库会被迁移，这是因为要占据换上的一段连续区间。
* 有什么缺陷？
    * 缺陷一：3台变4台，不够均匀。
    * 缺陷二：新机器的数据只从两台老机器上获取，导致这两台压力特别大。

# Slide 11 Consistent Hashing 更实用的方法

* 将整个hash区间看作是环。
* 环的大小从0-359变为0 - 2^64-1 。
* 把机器和数据都看作环上的点。
* 如何决定哪个数据存放哪个机器呢？
    * 给机器一个名字，算出hash value。
    * 来了一个数据1，算出hash value，顺时针去找下一台机器。
    * 这还是不能保证数据均匀
* micro shards/virtual nodes的概念。
    * 一台机器对应1000个micro shards/virtual nodes，洒在hash 环上。
    * 我的问题，如何算出这一千个micro shards/hash key?
    * 为什么不取1M micro shards?
* 需不需要把数据存在什么位置也存下来？
    * 我的答案：不用。需要找数据的时候，算一遍hash值即可。
* 怎么找机器？
    * 我的答案：存成一个sorted list, binary search可以找到顺时针的机器。
    * 错误：应该要用RB tree。log N 时间可以找到比当前key大的key。
* 加入新机器怎么办？
    * 先把机器变成1000个virtual nodes，在环上撒好。
    * 怎么要数据：
        * 我的想法，先找到下一个机器，遍历数据，找出小于新机器hash值的数据，移到
          新的机器上。
        * 我的问题：如何两个新机器撒到了同一个区间怎么办？
    * 怎样删数据：想法类似。
* 同学的问题1: 问什么是1000 virtual nodes? tradeoff, 1000机器就有1M 的nodes，treemap
  上就有1M的点。可能取1K 和 10K virtual nodes 均匀的程度是一样的。

# Slide 12 Replica 数据备份

* Backup 和 Replica 什么区别？
    * Backup 定期做，死数据，不用服务实时在线的东西。
    * Replica 同时做，活数据，在线。

# Slide 14 Backup VS Replica

* Backup
    * 周期性，e.g. 每天晚上进行一次备份。
    * 数据丢失，只能恢复到之前上一次的备份点。
    * 不用做在线数据服务，不分摊读。
* Replica
    * 实时的，数据写入时，会以复制品存成多分
    * 丢失时，马上可以通过其他复制品恢复
    * 用做在线数据服务，分摊读。
* 为啥还需要Backup
    * 价格
    * 双保险，better than nothing。

# Slide 15 MySQL Replica

* 自带master-slave replica 方法
* master 写， slave 读
* slave 从 master 同步数据。

# Slide 16 master - slave

* 原理 write ahead log
    * SQL 数据的任何操作，都会以log的形式做一份纪录。
    * log 内容：数据A在时刻B从C变成D
    * Master每次有任何操作就同志slave来读log
    * slave数据有延迟。
* master挂了怎么办
    * 一台slave升级成为master接受读写。
    * 可能会造成数据丢失，和不一致。

# Slide 17 NoSQL Replica

* 以Cassandra为代表的NoSQL数据库通常将数据顺时针存储在Consistent hashing环上的三个
  virtual nodes中。

# Slide 18 SQL vs NoSQL in Replica

* SQL
    * "自带"的replica方式是master slave
    * "手动"的replica方式也可以在Consistent hashing环上的三个virtual nodes中。
* NoSQL
    * "自带"的replica方式也可以在Consistent hashing环上的三个virtual nodes中。
    * "手动"的replica方式：就不需要手动，NoSQL就是在Sharding和Replica上帮你偷懒。

# Slide 19 设计短网址系统

* google 用6个字符。
* bitly 用7个字符。
* 大小写区分。

# Slide 20 短网址

* 一开始的想法可能是通过算法解决问题。

# Slide 21 系统设计的常见误区

* 一定不要这样假设：
    * 流量巨大无比
    * 要用NoSQL
    * 必须分布式
* 扔出一堆名词没有意义：load balancer, web server, memcached, NoSQL

# Slide 22 系统设计基本步骤

* 4S 分析法
* 1 Scenario: 功能/需求/QPS/存储容量
* 2 Service + Storage: 画图，根据分析结果设计可行解法。
* 3 Scale: 进化，研究可能遇到的问题，系统优化。

# Slide 23 场景分析

* `http://looooooooong.url` 转到 `http://short.url`
* 还要把短网址换成长网址，用户点击时。
* 用户把`http://www.jiuzhang.com`传给`http://bitly.com`, `bitly` 返回一个短网址。
* 第二种情况，用户把短网址给bitly，它返回长网址，用户再用长网址访问。
* QPS 是多少呢？
* 同学提问，数据库和文件系统的关系？
    * 数据库是文件系统的一层包装。最终还是存在文件系统中的。
    * 帮你实现feature, 管理数据。
    * 一台数据库不够用，怎么分在多台机器上，所以会出现consistent hashing.

# Slide 27 Scenario 需求 - QPS + Storage

* 日活跃用户：100M
* 推算产生一条tiny URL的QPS
    * 假设没人每天0.1条带URL的微博
    * Average QPS: 100M * 0.1 / 86400 ~ 100
    * Peak Write QPS: 100 * 2 = 200
* 点击一条tiny URL的QPS
    * 假设每人每天1个
    * avg: 1000
    * peak: 2000
* 推算每天产生新的URL的存储
    * 每天10M条
    * 每条100, 每天1G
    * 1T 硬盘用三年

# Slide 28 service

* 比较简单, 只有一个service， URL service

# Slide 29 service 逻辑块聚类与接口设计

* TinyURL只有一个URLService
* 函数设计

```
UrlService.encode(longurl)
UrlService.decode(shorturl)
```

* 访问端口设计
    * `GET /short_url`: return a http redirect response
    * `POST /data/shorten`: `DATA = {url: http://xxxx}`, return short url.

# Slide 30 数据存储与访问

* 第一步：select 选存储结果
* 第二步: schema 细化数据表

# SQL vs NoSQL 到底怎么选？

* 是否需要支持 transaction? - 不需要，NoSQL +1 (transaction see lecture 02)
    * NoSQL 不支持
* 是否需要支持丰富的SQL Query? - 不需要，NoSQL +1
    * NoSQL的SQL Query不够丰富
    * 也有一些NoSQL的数据库提供简单的SQL Query支持
* 是否想偷懒？- 不太重要。不复杂，NoSQL +1
    * 大多数web Framework和SQL数据库兼容的好
    * 用SQL少写代码
* 是否需要sequential ID? - 取决于算法
    * SQL提供了auto-increment的sequential ID，1，2，3，4，5
    * NoSQL ID不是sequential。分布式机器，分别制造id。UUID。自行google。
* 对QPS的要求多高？- QPS 不高，SQL +1
    * NoSQL 性能更高
* 对Scalability的要求多高？- 不高，SQL +1
    * SQL 需要码农自己写代码来scale: sharding/replica 。
    * NoSQL 帮你做了。

# Slide 37 Hash function (不可行)

* long url 的MD5后六位。
* 优点是快
* 缺点是难以设计一个没有冲突的哈希算法。

# Slide 38 随机生成shortURL + 数据库去重复

* 随机生产一个6位URL，如果没有被用过，就绑定到该longURL
* 优点：实现简单
* 缺点：网址越来多，生成越来越慢。
* 现实生活的例子：机票/酒店/确认码。就是这样操作。

# Slide 39 进制转换 Base62

* Base62
    * 将6位short url看作一个62进制的数
    * 每一个short url对应一个整数
    * 整数对应数据库表的primary key - sequential ID
* 优点，效率高
* 缺点：依赖于全局的自增ID。

# Slide 40 随机生成 v.s. 进制转换 都可以

# Slide 41 基于随机生成的方法

* 需要用short 查 long, 也需要用 long 查 short 。
* 如果用SQL型数据库，需要对shortkey 和 longurl 分别建索引。
* 什么是索引？http://t.cn/R6xgLD8
* 索引的原理？http://t.cn/R6xg4aj

* 如果是NoSql，那就建立两张表。
* 第一张表，`row_key=longURL, column_key=ShortURL, value=null or timestamp`
* 第二张表，`row_key=ShortURL, column_key=longURL, value=null or timestamp`

# Slide 44 基于进制转换的方法

* 因为需要用到自增ID，只能用SQL类型。（为什么？因为SQL型数据库能够用自增ID）
* 表单结构如下：

| id | longURL (index=true)    |
| :------------- | :------------- |
| 1       | http://www.jiuzhang.com       |

# Slide 49 How to reduce response time?

# Slide 50 如何提速

* 缓存提速：cache aside
    * 用户读的操作多
* 缓存存啥？
    * long to short (生成新的short url 需要，因为要看看有没有用过)
    * short to long (查询 short url 时需要)
* 过一段时间需不需要把url丢掉？
    * 如果始终没有访问
    * 我觉得不需要，disk is cheap。如果基于Sequential ID，删掉没有意义, 删掉的不能再利用。
    * 老师的意见是，还是不删好。
    * bitly删，给用户造成坏体验。
* Cassandra有一个功能是指定存的东西什么时候过期。

# Slide 51 如何提速 2

* 利用地理位置信息加速
    * 访问中国网址的短网址，先跑到美国服务器去解析短网址，就变慢了。
* 优化服务器访问速度
    * 不同的地区，使用不同的web服务器
    * 通过DNS解析不同地区的用户到不同的服务器
* 优化数据库访问速度
    * 使用Centralized MySQL + Distributed Memcached，Centralized MySQL 放在流量大
      的地方。
    * 中国的web server会去访问美国的数据服务器，这在很多问题上是不行的。但在tinyurl上可以。
      因为数据库的query太简单。服务器到服务器的路由跳转会少很多。
    * 一个MySQL 配多个memcached, memcached跨地区分布。
    * 老师建议，不要去做跨区域的备份。会被面试官面死。

# Slide 56 如何扩展

* 什么时候需要多台数据库服务器？
    * cache资源不够
    * 写操作越来越多
    * 越来越多的请求无法通过cache满足。
* 增加多台服务器到底是为了什么？
    * 数据存不下？- Storage 角度
    * 还是忙不过来？- QPS 角度 我觉得的是忙不过来。和老师一致。
      理由是，有可能读特别多，有人发起恶意写的攻击。写请求忙不过来，用数据库分担。

# Slide 57 如何扩展

* Vertical Sharding - 将多张数据表分配给多台机器
    * TinyURL 只有二张表或一张表
* Horizontal Sharding
    * 用什么东西做sharding ID。
    * 如果用ID, 如何查longURL。short to long 可以被优化。
        * 来了一个longURL，根本不知道在哪一个DB0/DB1/DB2里。
        * 所以没法创建longURL。
        * 一个不太好的解决办法，把地址广播出去。那就没有意义。没有起到sharding的作用。
        * 一个好一点的办法，不一定要一一对应。一个longURL可以存在多个DB里。只要保证短网址
          不要重复就好。当L->S查询的时候把longURL做sharding key。
    * 如果用longURL，如何查ID

# Slide 60 Scale - 扩展short key

* 最开始short key 是6位，加一位前置位。
* 前置位有hash(longURL)%62得到
* 前置位就是sharding key
* 无需广播
* short2long还是long2short都可以立刻找到数据所在服务器。

# Slide 64 Multi-Region的进一步优化

* 网站服务器和数据库服务器之间的通信
* 中心化服务器集群与跨地域的web server之间通信较慢
    * 中国服务器访问美国数据库
* 中国服务器访问中国数据库，重复写到中国数据库很难解决一致性的问题
* 用户习惯
    * 中国用户大多访问中国网站
    * 按照地域信息进行Sharding
        * 如何获得地域信息？把常用网址（top 10K）建一张表就好。
        * 我的问题：如果长网址，我们马上能知道要去中国的DB，还是美国的DB。可是short to long
          怎么办呢？
        * 老师的办法，也是用前置位来决定去访问美国还是中国。
    * 大部分（>90%）需求都可以在用户所在地域解决掉。
    * 这种sharding，DB CN 和 DN USA是不会重复的，所以不会有consistency的问题。
* 网上只能查到62进制，以下follow up只在课上可以学到
    * longURL需不需要一一对应
    * 需不需要删除数据
    * 地域性问题

# Slide 65 提供一个新的需求

* custom url
* `http://tiny.url/google => http://www.google.com`

# Slide 68 自定义短链接

* 新建一张表存储自定义URL: customURLTable

| custom url | long url (index=true)     |
| :------------- | :------------- |
| gg       | google.com       |
| jz       | jiuzhang.com       |

* 错误做法，开一个新的column。这样就好被浪费掉。
    * 数据很少出现
* 查询长链接
    * 先查询customURL
    * 再查询URL table
* 根据长链接创建普通短链接
    * 先查询customURL Table 是否存在
    * 再在URL table中查询和插入
* 创新自定义短链接
    * 先查询URL table中存在
    * 再在customURL Table中查询和插入

# Slide 70

* 没有唯一办法，言之有理即可
* 可行方法比fancy概念更有用

# Slide 71

* 留下的作业

# Q&A

* longURL这么长怎么做 sharding key?
    * `hash(longURL)`
* 别的类似于consistent hashing的算法？
    * google search `redis sharding 算法`
* Vertical V.S. Horizontal
    * User table: id/name/age/phone/email/password
    * 把 phone/email/password 单独拉出来 -》 vertical sharding
    * id0 去了 DB0, id1 去了 DB1。
* tinyURL 用几张表？
    * SQL数据库一张就可以
