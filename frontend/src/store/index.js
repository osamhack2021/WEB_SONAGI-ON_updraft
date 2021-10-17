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
    userdata: {},
    access_token: "",
    refresh_token: "",
  },
  mutations: {
    loginSuccess(state, payload) { // 로그인 성공시,
      state.isLogin = true;
      state.access_token = payload.access;
      state.refresh_token = payload.refresh;
    },
    refresh(state, payload){
      state.access_token = payload;
    },
    logout(state) { // 로그 아웃시,
      state.isLogin = false;
      state.userdata = {};
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
            this.dispatch('updateUserdata');
            resolve(true);
          })
          .catch((res) => {
            reject(res.data);
          });
      })
    },
    refresh({ commit }){
      if(this.state.isLogin){
        axios
          .post(`${this.state.BACKEND_URL}/api/user/refresh`, {'refresh' : this.state.refresh_token})
          .then((res) => {
            commit('refresh', res.data.access);
          })
          .catch(() => {
            this.dispatch('logout');
            this.$alert("세션이 만료되었습니다. 다시 로그인 해주세요.","","error");
          });
      }
    },
    logout({ commit }) {
      commit('logout');
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
    },
    updateUserdata({ commit }){
      const config = {
        headers: {
          Authorization: `Bearer ${this.state.access_token}`,
        },
      };
      axios.get(`${this.state.BACKEND_URL}/api/usersetting/get`, config)
        .then((res) => {
          commit('updateUserdata', res.data)
        })
        .catch((error) => {
          if(error.response.data.code === "token_not_valid"){
            this.dispatch('logout');
            this.$alert("세션이 만료되었습니다. 다시 로그인 해주세요.","","error");
          } else {
            this.dispatch('logout');
            this.$alert("[STORE001] 예상치 못한 에러가 발생했습니다.","","error");
          }
        })
    }
  },
});