		<script>
			var vm = new Vue({
				el:'#app',
				data:{
					list:[
						{
							id:1,
							name:'张三',
							pname:'手机支架',
							price:6,
							count:0
						},
						{
							id:2,
							name:'王五',
							pname:'旧手机小米6',
							price:700,
							count:0
						},
						{
							id:3,
							name:'小六',
							pname:'久笔记本',
							price:2000,
							count:0
						}
					]
				},
				computed:{
					totalPrice:function(){
						var total = 0;
						for(var i = 0;i<this.list.length;i++){
							var item = this.list[i];
							total += item.price*item.count;
						}
						return total.toString();
					}
				},
				methods:{
					handleReduce:function(index){
						if(this.list[index].count ===0)return;
						this.list[index].count--;
					},
					handleAdd:function(index){
						this.list[index].count++;
					},
					handleRemove:function(index){
						this.list.splice(index,1);
					}
				}
			});
		</script>