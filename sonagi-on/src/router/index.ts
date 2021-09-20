import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import LoginView from '../views/LoginView.vue';
import MainView from '../views/MainView.vue';
import SignupView from '../views/SignupView.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: MainView,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupView,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
