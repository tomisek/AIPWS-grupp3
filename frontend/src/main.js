import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import store from './store.js'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import router from './router'

const app = createApp(App)

app.use(router)
app.use(store)

app.mount('#app')
