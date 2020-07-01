import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import router from './router';
import iView from 'iview';
import 'iview/dist/styles/iview.css';
import axios from 'axios';
import vueAxios from 'vue-axios';
import store from './store';
import Vuex from 'vuex'

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(iView)
Vue.use(vueAxios,axios)
Vue.use(Vuex)

router.afterEach(route=>{
	window.scroll(0,0);
})

router.beforeEach((to,from,next)=>{
	let token = localStorage.getItem('Authorization');
	if(!to.meta.isLogin){
		next()
	}else{
		let token = localStorage.getItem('Authorization');
		if(token == null || token == ''){
			next('/')
		}else{
			next()
		}
	}
})

axios.interceptors.request.use(
	config => {
		let token = localStorage.getItem('Authorization');
		if(token){
			config.headers.common['token'] = token
		}
		return config
	},
	err => {
		return Promise.reject(err);
	});


new Vue({
  el:'#app',
  render: h => h(App),
  router,
  store,
})

