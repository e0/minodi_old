// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueAnalytics from 'vue-analytics'
import axios from 'axios'
import App from './App'
import router from './router'

Vue.config.productionTip = false
axios.defaults.baseURL = '/api'

Vue.use(VueAnalytics, {
  id: 'UA-98400512-1',
  router
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})

