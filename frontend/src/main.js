import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import store from './store.js'

const app = createApp(App)
app.use(store)
app.mount('#app')
