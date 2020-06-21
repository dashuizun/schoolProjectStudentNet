# schoolProjectStudentNet
# 1.	项目简介

项目四 ：学生校园网

简介：介绍思路和整体要求 该项目为针对校园学生的网站，设计学生共同关注的信息服务及论坛。 业务场景：描述相关的真实企业业务背景。从真实场景中，适当简化或者提炼出适合项目场景 学生校园网是以全国各类学校为信息节点的校园社区平台，关注学生创业、就业、生活、情感、心理、学习、留学。提供服务及论坛。

功能性需求 基本功能： 1.实现基本公共信息服务； 2.实现学生论坛服务； 3.实现学生二手市场服务；

扩展功能 ：根据校园情景，提供1到2项扩展服务（可加分）

非功能性需求 1.代码要有规范的说明文档； 2.所有代码要注明具体开发人员 ；

其他限制条件：开发环境、实验平台、开发语言、数据库、编译器等限制条件 服务器： windows操作系统， Flask服务器或其它。

开发语言 ： javascript , Python或其他

开发工具： Hbuilder或其它

数据库 ： mysql

测试数据或平台： 测试环境： 1.移动客户端基于Android或IOS，或移动端浏览器均可； 2.pc端环境以IE、FireFox、Chrome主流浏览器为主。 其他要求

# 2.  项目结构

- 目录

  ```html
  │  front.rar
  │  GITHUB操作.docx
  │  list.txt
  │  README.md
  │  新建文本文档.txt
  │  说明文档.docx
  │  
  ├─back	后端项目
  │  │  config.py	配置文件
  │  │  myapp.py	启动程序
  │  │     
  │  ├─app	项目代码文件夹
  │  │  │  models.py	模型
  │  │  │  __init__.py	构造文件
  │  │  │  
  │  │  ├─api	接口文件夹
  │  │  │  │  communityApi.py	用户交流平台接口
  │  │  │  │  loginregistApi.py	登录注册接口
  │  │  │  │  productApi.py	二手市场接口
  │  │  │  └─__init__.py	构造文件
  │  │  │          
  │  │  └─main	主文件夹
  │  │      │  views.py	视图页面
  │  │      └─__init__.py	构造文件
  │  │          
  │  └─venv	虚拟环境
  │
  └─front
      │  communityHt.html	用户交流页面
      │  dataInsert.html
      │  index.html	主页
      │  login.html	注册页面
      │  regist.html	登录页面
      │  productHt.html	二手市场页面
      │  
      ├─config	配置文件夹
      ├─scr
      └─static	静态文件夹
          ├─css	css文件夹
          │      productHt.css	二手市场CSS文件
          │      
          ├─img	图片文件夹
          └─js	js文件夹
                  vue-resource.min.js
                  vue.js
  ```

  

# 3.  数据库配置

### 1.	账号密码配置

```mysql
mysql -u root -p
账号：root
密码：123456
```

### 2.	创建并配置用户表

- 创建用户表并添加数据

  ```mysql
  USERS
  ID 序号
  NAME 用户名
  PASSWORD 密码
  EMAIL 电子邮箱
  CREATE TABLE users(ID INT NOT NULL AUTO_INCREMENT,NAME VARCHAR(20) NOT NULL,PASSWORD VARCHAR(50) NOT NULL,EMAIL VARCHAR(100) ,PRIMARY KEY (ID));
  INSERT INTO users(ID,NAME,PASSWORD,EMAIL)VALUES(1,"管理员","123456","1534273733@qq.com");
  INSERT INTO users(ID,NAME,PASSWORD,EMAIL)VALUES(2,"用户1","12345","153427373@qq.com");
  INSERT INTO users(ID,NAME,PASSWORD,EMAIL)VALUES(3,"用户2","1234","15342737@qq.com");
  ```

- 创建市场产品表

  ```mysql
  PRODUCT
  ID 序号
  NAME 卖家的用户名
  PNAME 产品名
  PRICE 价格
  DESCRIPTION 产品描述
  CREATE TABLE PRODUCT(ID int NOT NULL ,NAME varchar(20) NOT NULL ,PNAME varchar(20) NOT NULL ,PEICE int NOT NULL ,DESCRIPTION varchar(100) NULL ,PRIMARY KEY (ID));
  INSERT INTO PRODUCT(ID,NAME,PNAME,PEICE,DESCRIPTION)VALUES(1,"管理员","二手小米6",500,"用过几个月，成新，买了新手机打算换掉");
  INSERT INTO PRODUCT(ID,NAME,PNAME,PEICE,DESCRIPTION)VALUES(2,"用户1","全新公牛插排",20,"不小心买多了个插排，全新的公牛！");
  INSERT INTO PRODUCT(ID,NAME,PNAME,PEICE,DESCRIPTION)VALUES(3,"用户2","全新TYPE-C充电线",10,"全新的充电线线");
  
  ```

- 创建论坛帖子表

  ```mysql
  COMMUNITY
  ID 序号
  NAME 发帖人的用户名
  PNAME 帖子内容
  CREATE TABLE COMMUNICATION(ID int NOT NULL ,NAME varchar(20) NOT NULL ,DESCRIPTION varchar(100) NULL ,PRIMARY KEY (ID));
  INSERT INTO COMMUNICATION(ID,NAME,DESCRIPTION)VALUES(1,"管理员","这交流平台真好用！！！");
  INSERT INTO COMMUNICATION(ID,NAME,DESCRIPTION)VALUES(2,"用户1","有人吗？有人吗？有人吗？有人吗？");
  INSERT INTO COMMUNICATION(ID,NAME,DESCRIPTION)VALUES(3,"用户2","呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐");
  ```

# 4.  软件配置

# 5.  后端开发说明

# 6.  前端开发说明

# 7.  开发人员汇总

