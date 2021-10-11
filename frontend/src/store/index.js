import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import createPersistedState from 'vuex-persistedstate';
import router from '../router';

Vue.use(Vuex);

const BACKEND_URL = 'https://osamhack2021-web-sonagi-on-updraft-66vr695xc4qg6-8000.githubpreview.dev';

export const store = new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    isLogin: false,
  },
  mutations: {
    loginSuccess(state) { // 로그인 성공시,
      state.isLogin = true;
    },
    logout(state) { // 로그 아웃시,
      state.isLogin = false;
    },
  },
  actions: {
    login(dispatch, loginObj) {
      axios
        .post(`${BACKEND_URL}/api/user/login/`, loginObj)
        .then((res) => {
          localStorage.setItem('access_token', res.data.access_token);
          localStorage.setItem('refresh_token', res.data.refresh_token);
          this.commit('loginSucess')
          router.push({ name: '대시보드' });
        })
        .catch(() => {
          // todo : 응답에 맞게 alert 띄우기
          alert('이메일과 비밀번호를 확인하세요.');
        });
    },
    logout({ commit }) {
      commit('logout');
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      router.push({ name: '대시보드' });
    },
    signup(dispatch, signupObj) {
      axios
        .post(`${BACKEND_URL}/api/rest-auth/registration/`, signupObj)
        .then(() => {
          alert('회원가입이 성공적으로 이뤄졌습니다.');
          router.push({ name: '대시보드' });
        })
        .catch(() => {
          // todo : 응답에 맞게 alert 띄우기
          // todo : signup은 Register.vue에 넣자. 왜? -> 잘못된 입력에 대해서 응답으로 온 에러를 alert 말고 입력칸 위에 빨갛게 띄워주는게 나을듯. 어차피 commit도 안함.
          alert('에러');
        });
    },
  },
});