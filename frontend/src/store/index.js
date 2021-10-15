import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import createPersistedState from 'vuex-persistedstate';
// import router from '../router';

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    BACKEND_URL : 'https://sonagi.run.goorm.io',
    isLogin: false,
    access_token: "",
    refresh_token: "",
  },
  mutations: {
    loginSuccess(state, payload) { // 로그인 성공시,
      state.isLogin = true;
      state.access_token = payload.access;
      state.refresh_token = payload.refresh;
    },
    logout(state) { // 로그 아웃시,
      state.isLogin = false;
      state.access_token = "";
      state.refresh_token = "";
    },
  },
  actions: {
    login({ commit }, loginObj) {
      return new Promise((resolve, reject) => {
        axios
          .post(`${this.state.BACKEND_URL}/api/user/login`, loginObj)
          .then((res) => {
            commit('loginSuccess', res.data);
            resolve(true);
          })
          .catch((res) => {
            reject(res.data);
          });
      })
    },
    logout({ commit }) {
      commit('logout');
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
    },
  },
});