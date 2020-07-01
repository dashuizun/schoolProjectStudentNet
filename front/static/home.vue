<template>
	<div class="super">
		<div class="header">
			<div class="buttomDiv">
				<Button type="success" class="loginButton" @click="showLoginModal">Login</Button>
				<Button type="primary" class="loginButton" @click="showRegisterModal">Register</Button>
			</div>
		</div>

		<div class = "content">
			<div class="contentLeft">
				<div
					v-for = "post in blogList"
					>
					<thumbnail 
						v-bind:title=post.title
						v-bind:content=post.content
					></thumbnail>
				</div>
			</div>
			<div class="contentRight"></div>
			
		</div>

		<Modal v-model="registerModalStatus" @on-ok="registerEvent">
			<p>Register</p>
			<Input v-model="username" placeholder="Username" style="width: 300px" />
			<Input v-model="password" placeholder="Password" style="width: 300px" />
		</Modal>

		<Modal v-model="loginModalStatus" @on-ok="loginEvent">
			<p>Login</p>
			<Input v-model="username" placeholder="Username" style="width: 300px" />
			<Input v-model="password" placeholder="Password" style="width: 300px" />
		</Modal>

	</div>
</template>

<script>
	import axios from 'axios'
	import {mapMutations} from 'vuex'
	import store from '../store'
	import thumbnail from './articleThumbnail.vue'

	export default{
		name: 'home',
		data:function(){
			return {
				loginModalStatus:false,
				registerModalStatus:false,
				username:'',
				password:'',
				blogList:'',
			}
		},
		components:{
			thumbnail:thumbnail,
		},
		created(){
			localStorage.removeItem("Authorization","")
			let _this = this
			axios.get('http://127.0.0.1:5000/postlist')
					.then(function(response){
						_this.blogList = response.data.posts
					})
					.catch(function(error){
					})
		},
		methods:{
			...mapMutations([
				'changeLogin'
			]),
			showRegisterModal:function(){
				this.registerModalStatus = true;
			},
			showLoginModal:function(){
				this.loginModalStatus = true;
			},
			registerEvent:function(){
				let that = this
				axios.post('http://127.0.0.1:5000/register',{
					username:this.username,
					password:this.password,
					})
				.then(function(res){

				})
				.catch(function(error){

				})
			},
			loginEvent:function(){
				let _this = this
				axios.post('http://127.0.0.1:5000/login',{
							username:this.username,
							password:this.password,
						})
					.then(function(response){
						let token = response.data
						_this.changeLogin({Authorization: token})
					})
					.catch(function(error){
					})
			},
			navigator:function(){
				this.$router.push("/article")
			},

		},
	}
</script>

<style scoped>

</style>

