import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import createPersistedState from 'vuex-persistedstate';
import router from '../router';

Vue.use(Vuex);

const BACKEND_URL = 'https://osamhack2021-web-sonagi-on-updraft-66vr695xc4qg6-8000.githubpreview.dev';

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    userInfo: null, // 아직 정보를 받아오지 않은 상태이므로 null
    isLogin: false, // 로그인이 되었다면 true로 변경
    isLoginError: false,
  },
  mutations: {
    loginSuccess(state, payload) { // 로그인 성공시,
      state.isLogin = true;
      state.isLoginError = false;
      state.userInfo = payload;
    // payload 에 대한 정보는 위키피디아를 참고했다. 쉽게 말해 userInfo에 배정되는 실제 유저 정보를 할당한다고 보면 된다.
    },
    loginError(state) { // 로그인 실패시,
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    },
    logout(state) { // 로그 아웃시,
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    },
  },
  actions: {
    login(dispatch, loginObj) {
    // login --> 토큰 반환
      axios
        .post(`${BACKEND_URL}/api/rest-auth/login/`, loginObj)
        // loginObj = {email,password}를 받아온다.
        .then((res) => {
          // 접근 성공시, 토큰 값이 반환된다. (실제로는 토큰과 함께 유저 id를 받아온다.)
          // 토큰을 로컬 스토리지에 저장
          localStorage.setItem('access_token', res.data.token); // 로컬 스토리지에 토큰 저장
          this.dispatch('getMemberInfo');
          router.push({ name: 'Home' });
        })
        .catch(() => {
          alert('이메일과 비밀번호를 확인하세요.');
        });
    },
    logout({ commit }) {
      commit('logout');
      localStorage.removeItem('access_token');
      router.push({ name: 'Home' });
    },
    signup(dispatch, signupObj) {
      axios
        .post(`${BACKEND_URL}/api/rest-auth/registration/`, signupObj)
        // loginObj = {email,password}
        .then((res) => {
          alert('회원가입이 성공적으로 이뤄졌습니다.');
          router.push({ name: 'login' });
          console.log(res);
        })
        .catch(() => {
          alert('이메일과 비밀번호를 확인하세요.');
        });
    },
    getMemberInfo({ commit }) {
      // 로컬 스토리지에 저장된 토큰을 저장한다.
      const token = localStorage.getItem('access_token');
      const config = {
        headers: {
          Authorization: `jwt ${token}`,
        },
      };
      // 토큰 -> 멤버 정보 반환
      // 새로고침 --> 토큰만 갖고 멤버 정보 요청가능
      axios
        .get(`${BACKEND_URL}/api/user/`, config)
        .then((res) => {
          const userInfo = {
            username: res.data.username,
          };
          commit('loginSuccess', userInfo);
        })
        .catch(() => {
          alert('이메일과 비밀번호를 확인하세요.');
        });
    },
  },
});
