
# Useful links

# Slide 02

* 什么是分布式系统？
    * 用多台机器解决一台机器不能解决的问题
    * 存储不够
    * QPS不够
    * Google 做法，多用便宜机器。面临新问题，便宜机器经常坏，需要调换。
    * Sun 做法，超级计算机。

# Slide 03 Overview

* Distributed File system (Google File system)
    * 怎么样有效存储数据？
    * No SQL 底层需要一个文件系统
* Map Reduce
    * 怎么快速处理数据
* bigtable = No-SQL Database
    * 怎么连接底层存储和上层数据

# Slide 05 你会掌握

* master slave pattern
* How to check system failure and error
    * Google 买了便宜的机器
* How to design Distributed file system

# Slide 06 了解了之后可以做什么？

* Google / MS 面试会遇到
* 对学习系统有帮助
    * 如何处理failure和recovery

# Slide 07 Distributed File System

* GFS by google, not open source
* HDFS by Yahoo, open source (Hadoop Distributed File System)

# Slide 08 Overview

* 4S 分析
* Scenario
* service
* Storage
    * Chrome 输入google.com，访问google web server, web server 访问database.
    * database 存在 gfs 里面。

# Slide 09 场景分析 scenario

* 需要哪些功能
    * 用户写入一个文件，用户读取一个文件
    * 支持多大的文件？本地机器上大概100Mb, 1G。G家F家都是 > 1000TB
* 需求2
    * 多台机器存储这些文件
    * 支持多少台机器？2007年10万台。

# Slide 11 Service

* Client + Server
* client 是个啥？client 是 websever 和 DB.
* 多台机器怎么沟通？
    * 社会主义
    * 资本主义

# Slide 15

* Peer to peer: server 级别都一样。
    * shortage: 同步问题
* master oversees all slave servers, client talk to master
    * 缺点一，master dies, everyone dies
    * 优点，同步相对简单。

# Slide 17

|                | DB             | GFS |
| :------------- | :------------- | :-- |
| Master         | 存储数据        | 管理者（不存储数据）|
| Slave          | Backup         | 被管理者（存储实际文件, partition）|

# Slide 19 Storage

* Peer to peer (Bitcomet, Cassandra, 不是重点，考察少)。
    * Advantage
        * 一台机器挂了，还能用。
    * Disadvantage
        * 数据一致
* Master slave
    * Advantage
        * Simple design
        * 数据很容易保持一致
    * Disadvantage
        * 单master要挂
* Final decision
    * Master + Slave
        * 如何保持数据一致性，client 只写给master，master 决定写到哪个slave。
        * 最后可以看paper。

# Slide 20 Storage

* 大文件存在哪儿？
    * 内存？数据库？文件系统？
    * 我觉得应该存在文件系统里。
    * 内存不够大。数据库适合存结构化的东西。
    * 大文件非结构化。
    * 什么是结构化？比如一个人的信息有姓名，年龄，生日。
    * 那么一张图片的内容没有什么结构。
* 怎么存在文件系统？
    * 操作系统知识怎么存文件？

# Slide 22 存一个单一文件

* 普通文件100G。
* 存储哪些信息？
    * 文件内容本身
    * meta data：像日期/格式/大小
