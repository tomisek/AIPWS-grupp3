import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Predict from './views/Predict.vue'
import Statistics from './views/Statistics.vue'
import Artists from './views/Artists.vue'

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
    },
    {
        name: 'Artists',
        path: '/artists',
        component: Artists
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router