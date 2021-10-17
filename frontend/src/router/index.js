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
        name: '대시보드',
        component: Dashboard
    },
    {
        path: '/diary',
        name: '나의 연대기',
        component: Diary,
    },
    {
        path: '/diary-write',
        name: '일기 쓰기',
        component: DiaryWrite
    },
    {
        path: '/diary-manage',
        name: '일기 관리',
        component: DiaryManage
    },
    {
        path: '/calendar',
        name: '캘린더',
        component: Calendar
    },
    {
        path: '/community',
        name: '커뮤니티',
        component: Community
    },
    {
        path: '/event',
        name: '공모전/행사',
        component: Event
    },
    {
        path: '/self-care',
        name: '자기관리',
        component: SelfCare
    },
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router