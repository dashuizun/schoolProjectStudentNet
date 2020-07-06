```PYTHON
			var vue = new Vue({
				el: '#app',
				data: {
					loginN: [],
				},
				mounted: function() {
					this.gett()
				},
				methods: {
					gett:function() {
						var self = this;
						//在编译后即调用API接口取得服务器端数据
						self.$http.get('/todo/api/getLoginApi').then(function(res) {
							self.loginN = res.data.loginnName;
						},function(){
		                        console.log('请求失败处理');
		                    });
					},
				}
			})
```

```
				mounted: function() {
					this.gett()
				},
```

		<script src="js/vue.js"></script>
		<script src="js/vue-resource.min.js"></script>
		<div id="app" v-cloak>
		</div>

```
									<li>
										<a>当前用户：{{ loginN[0].lname }}</a>
									</li>
									<li>
										<a href="/logout">登出</a>
									</li>
```

