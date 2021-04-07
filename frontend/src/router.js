import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Predict from './views/Predict.vue'
import Statistics from './views/Statistics.vue'
import Viewstat from './components/Viewstat.vue'

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
        component: Statistics,
        children: [

            { path: '/statistics/viewstat', component: Viewstat },

            // { path: 'artists', component: Artists}

        ]
    },

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router