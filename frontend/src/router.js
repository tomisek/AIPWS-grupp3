import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Predict from './views/Predict.vue'
import Statistics from './views/Statistics.vue'
import Artists from './views/Artists.vue'
import Viewstat from './views/Viewstat.vue'
import Genre from './views/Genre.vue'


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

            { path: '/statistics/artists', component: Artists},

            { path: '/statistics/genre', component: Genre}

        ]
    },

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router