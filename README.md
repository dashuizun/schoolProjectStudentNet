# mysql-flask-vue-schoolProjectStudentNet

# 1.	项目简介

## 学生校园网

<font color='#FE642E' size=6>vue+flask 前后分离式</font>

<font color='#FE642E' size=4>介绍思路和整体要求 该项目为针对校园学生的网站，设计学生共同关注的信息服务及论坛。 业务场景：描述相关的真实企业业务背景。从真实场景中，适当简化或者提炼出适合项目场景 学生校园网是以全国各类学校为信息节点的校园社区平台，关注学生创业、就业、生活、情感、心理、学习、留学。提供服务及论坛。</font>

## 功能性需求

<font color='#FE642E' size=6>1.实现基本公共信息服务；</font> 

<font color='#FE642E' size=6>2.实现学生论坛服务；</font> 

<font color='#FE642E' size=6>3.实现学生二手市场服务；</font>

## 开发语言

<font color='#FE642E' size=6> javascript </font>

<font color='#FE642E' size=6>html </font>

<font color='#FE642E' size=6>python</font>

<font color='#FE642E' size=6>mysql</font>

# 2.  项目结构

- 目录

  ```html
  ├─back	后端项目
  │  │  
  │  │  myapp.py	启动程序
  │  │     
  │  ├─app	项目代码文件夹
  │  │  │  config.py	配置文件
  │  │  │  models.py	模型
  │  │  └─ __init__.py	构造文件
  │  │  │  
  │  │  ├─api	接口文件夹
  │  │  │  │  communityApi.py	用户交流平台接口
  │  │  │  │  loginRegistApi.py	登录注册接口
  │  │  │  │  productApi.py	二手市场接口
  │  │  │  └─ __init__.py	构造文件
  │  │  │          
  │  │  └─main	主文件夹
  │  │      │  views.py	视图页面
  │  │      └─ __init__.py	构造文件
  │  │          
  │  └─venv	虚拟环境
  │
  └─front
      │  communityHt.html	评论页面
      │  cs.html	测试页面
      │  login.html	登录页面
      │  lunIndex.html	论坛主页
      │  myZhuye.html	个人主页
      │  productHt.html	二手市场
      │  regist.html	注册
      │  single.html	页面
      │  single1.html	页面
      │  single2.html	页面
      │  single3.html	页面
      │  style2.css
      │  
      ├─CS
      │      chuan.html
      │      communityHt.html
      │      index.html
      │      login.html
      │      productHt.html
      │      regist.html
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
  CREATE TABLE PRODUCT(ID int NOT NULL ,NAME varchar(20) NOT NULL ,PNAME varchar(20) NOT NULL ,PRICE int NOT NULL ,DESCRIPTION varchar(100) NULL ,PRIMARY KEY (ID));
  INSERT INTO PRODUCT(ID,NAME,PNAME,PRICE,DESCRIPTION)VALUES(1,"管理员","二手小米6",500,"用过几个月，成新，买了新手机打算换掉");
  INSERT INTO PRODUCT(ID,NAME,PNAME,PRICE,DESCRIPTION)VALUES(2,"用户1","全新公牛插排",20,"不小心买多了个插排，全新的公牛！");
  INSERT INTO PRODUCT(ID,NAME,PNAME,PRICE,DESCRIPTION)VALUES(3,"用户2","全新TYPE-C充电线",10,"全新的充电线线");
  ```

- 创建论坛帖子表

  ```mysql
  COMMUNITY
  ID 序号
  NAME 发帖人的用户名
  DESCRIPTION 帖子内容
  CREATE TABLE COMMUNITY(ID int NOT NULL ,NAME varchar(20) NOT NULL ,DESCRIPTION varchar(100) NULL ,PRIMARY KEY (ID));
  INSERT INTO COMMUNITY(ID,NAME,DESCRIPTION)VALUES(1,"管理员","这交流平台真好用！！！");
  INSERT INTO COMMUNITY(ID,NAME,DESCRIPTION)VALUES(2,"用户1","有人吗？有人吗？有人吗？有人吗？");
  INSERT INTO COMMUNITY(ID,NAME,DESCRIPTION)VALUES(3,"用户2","呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐呐");
  ```

# 4.  API接口

### 评论区接口

```python
# 获取数据
@api.route('/todo/api/communityApi', methods=['GET'])
# 添加数据
@api.route('/todo/api/addCommunityApi', methods=['POST'])
```

### 二手市场接口

```python
# 获取数据
@api.route('/todo/api/Productions', methods=['GET'])
# 添加数据
@api.route('/todo/api/addProduction', methods=['POST'])
# 删除数据
@api.route('/todo/api/deleteProduction', methods=['POST'])
```

### 登录注册接口

```python
# 获取登录状态
@api.route('/todo/api/getLoginApi', methods=['GET'])
# 注册接口
@api.route('/todo/api/addRegistApi', methods=['POST'])
# 登录接口
@api.route('/todo/api/loginApi', methods=['GET', 'POST'])
```

# 5. 后端部分说明

## myapp.py

```python
# 屏蔽JINJA2 防止和VUE冲突
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'
```

### app/models.py

```python
# 将数据库数据转换为JSON格式
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, o)
    
# 重构Flask
class Flask(_Flask):
    json_encoder = JSONEncoder
    
# 设置用户模型
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(128))
    # 判断登录状态
    def is_authenticated(self):
        return True
```

#### 1. 从数据库中获取数据然后转换为JSON格式

```python
# 将数据发送到URL地址中
@api.route('/todo/api/Productions', methods=['GET'])
def getTasks():
    # 获取Product表中的所有数据
    test_data = Product.query.all()
    # 将数据库的数据转换为JSON格式
    Production = json.loads(json.dumps(test_data, cls=JSONEncoder))
    # 将数据返回到URL地址中
    return jsonify({'productH': Production})
```

#### 2. 从前端获取数据 然后 添加到数据库中

```python
    # 获取数据 然后 添加到市场模型
    tas = Product(id=Production[-1]['id'] + 1, name=name, pname=request.json.get('pname', ""), description=request.json.get('description', ""), price=request.json.get('price', ""), )
    # 添加数据到数据库中
    db.session.add(tas)
    db.session.commit()
    # 将数据添加到json列表中
```

#### 3. 从前端获取到需要删除的数据 然后删除该数据

```python
    # 获取前端中需要删除的数据
    task_id = request.json['id']
    for task in Production:
        if task['id'] == task_id:
            Production.remove(task)
            # 找到该条数据
            test_data = Product.query.filter(Product.id == task_id).first()
            # 删除该条数据
            db.session.delete(test_data)
            db.session.commit()
            return jsonify({'productH': Production})
```

#### 4. 判断当前登录状态

```PYTHON
    loginnName = [{'lname': '游客'}]
    # 如果已经登录，那么获取登录用户名，否则默认
    if current_user.is_authenticated:
        loginnName[0]['lname'] = current_user.get_id()
```

#### 判断从前端获取到的用户名和密码是否正确

```python
# 登录接口
@api.route('/todo/api/loginApi', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 获取前端数据
        user_id = request.json.get('name')
        user_pw = request.json.get('passwor')
        # 将数据给到query_user方法找到该条记录
        user = query_user(user_id)
        # 如果user不为空且密码正确
        if user is not None and user_pw == user['password']:
            print('信息----------成功登陆------------')
            curr_user = User()
            curr_user.id = user_id
            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user)
            return jsonify({'code': 200, 'name': user_id})

    # GET 请求
    return 'cs %s' % current_user.get_id()


def query_user(user_name):
    for user in json.loads(json.dumps(User.query.all(), cls=JSONEncoder)):
        if user_name == user['name']:
            return user
```

# 6. 前端部分说明

### 获取到后端数据并打开网页是默认渲染

```javascript
mounted: function() {
   this.gett()
},
methods: {
   gett: function() {
      var self = this;
      //在编译后即调用API接口取得服务器端数据
      self.$http.get('/todo/api/Productions').then(function(res) {
         self.productH = res.data.productH;
      });
   },
}
```

### 将前端获取到的数据返回给后端

```HTML
// HTML
<p>商品名称：<input type="text" v-model="new_prod.pname"></p>
<p>商品描述：<input type="text" v-model="new_prod.description"></p>
<p>商品价格：<input type="number" v-model="new_prod.price"></p>
<button @click="addTask">确认发表商品</button>
```

```js
// JS
<script>
			var vue = new Vue({
				el: '#app',
				data: {
					productH: [],
					new_prod: {
						name: '',
						pname: '',
						description: '',
						price: 0
					}
				},
				methods: {
					addTask: function() {
						var self = this;
						self.$http.post('/todo/api/addProduction', {
							pname: self.new_prod.pname,
							description: self.new_prod.description,
							price: self.new_prod.price
						}).then(function(res) {
							self.productH = res.data.productH;
						});
					},
			})
</script>
```
