import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '@/views/Dashboard'
import Diary from '@/views/Diary'
import DiaryWrite from '@/views/DiaryWrite'
import DiaryManage from '@/views/DiaryManage'
import Calendar from '@/views/Calendar'
import Community from '@/views/Community'
import Event from '@/views/Event'
import SelfCare from '@/views/SelfCare'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Dashboard',
        component: Dashboard
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard
    },
    {
        path: '/diary',
        name: 'Diary',
        component: Diary
    },
    {
        path: '/diary-write',
        name: 'DiaryWrite',
        component: DiaryWrite
    },
    {
        path: '/diary-manage',
        name: 'DiaryManage',
        component: DiaryManage
    },
    {
        path: '/calendar',
        name: 'Calendar',
        component: Calendar
    },
    {
        path: '/community',
        name: 'Community',
        component: Community
    },
    {
        path: '/event',
        name: 'Event',
        component: Event
    },
    {
        path: '/self-care',
        name: 'SelfCare',
        component: SelfCare
    },
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router