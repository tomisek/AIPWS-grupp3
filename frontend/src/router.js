import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Predict from './views/Predict.vue'
import Statistics from './views/Statistics.vue'

const routes = [
    {
        name: 'Home',
        path: '/',
        component: Home
    },
    {
        name: 'Predict',
        path: '/predict',
        component: Predict
    },
    {
        name: 'Statistics',
        path: '/statistics',
        component: Statistics
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router