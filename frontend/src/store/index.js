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
    userInfo: {
    }, // 아직 정보를 받아오지 않은 상태이므로 null
    isLogin: false, // 로그인이 되었다면 true로 변경
    isLoginError: false,
    rcData : {
        discharge_P : 0, //전역일 퍼센트
        promotion_P : 0, // 다음 계급 진급일 퍼센트
        step_P : 0,     // 다음 호봉 진급일 퍼센트
        currentDays : 0, // 현재 복무일
        remainDays : 0,  // 남은 복무일
        promotion : 0,   // 다음 계급 진급일
        step : 0,       // 다음 호봉 진급일
        serviceDays : 0, // 전체 복무일
        rankIdx : 0,      // 사용자의 현재 계급idx
        nmRankIdx :0,      //사용자의 현재 계급idx
        stepIdx : 0,      // 사용자의 현재 호봉
        nmStepIdx : 0,     // 사용자음 다음 호봉
        nmHouse : false,   // 다음 달에 전역일 경우
    },
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
    updateRcData(state,payload){

        var dateDiff = (a,b) =>{
          return (a.getTime()-b.getTime())/(1000*3600*24);
        }
        
        state.userInfo = payload;

        var tmp = []; //진급일 배열을 임시로 저장할 배열
        var idx = 0;  // 사용자의 현재 계급의 인덱스
        var today = new Date(); 
        payload.days.forEach((item)=> {         //tmp를 date객체를 가진 배열로 만들어 준다.
            var list = item.split("-");
            tmp.push(new Date(list[0],list[1]-1,list[2]));
        });
        var all = Math.floor(dateDiff(tmp[4],tmp[0]));//총 복무일
        state.rcData.serviceDays = all;       

        var cur = Math.floor(dateDiff(today,tmp[0])); //현재 복무일
        state.rcData.currentDays = cur;

        state.rcData.discharge_P = Math.round((dateDiff(today,tmp[0]) / all *100)*1000000)/1000000; //전역일 퍼센트
        console.log(state.rcData.discharge_P);
        /*----------------------------------------------------------------------------------------*/

        state.rcData.remainDays = (all - cur);                     //남은 복무일

        for(var i=0;i<4;i++){ //현재 계급 구하기
          if(tmp[i].getTime()<=today.getTime() && tmp[i+1].getTime()>today.getTime()){
            idx = i;
            break;
          }
        }
        state.rcData.rankIdx = idx;

        var prom = dateDiff(tmp[idx+1],today)+1; //다음 계급 진급일
        state.rcData.promotion = prom;
        var prodiff = dateDiff(tmp[idx+1],tmp[idx]) // 현재 계급 진급일과 다음 계급 진급일 일수 차 구하기

        state.rcData.promotion_P = Math.round(((prodiff-prom)/prodiff *100)*1000000)/1000000; // 다음계급 진급일 퍼센트

         /*----------------------------------------------------------------------------------------*/

        var curStep = today.getMonth() - tmp[idx].getMonth() +1;  // 현재 호봉 수
        state.rcData.stepIdx = curStep;
        if(today.getMonth()+1 == tmp[idx+1].getMonth()){ //다음달이 진급일이라 호봉 수가 1로 바뀔 때
          if(idx == 3){
            state.rcData.nmStepIdx = curStep+1;
            state.rcData.nmRankIdx = state.rcData.rankIdx;
          }else{
            state.rcData.nmStepIdx = 1;
            state.rcData.nmRankIdx = state.rcData.rankIdx +1;
            }
        } else {        
          state.rcData.nmStepIdx = curStep+1;
          state.rcData.nmRankIdx = state.rcData.rankIdx;
        }


        var tm = new Date(today.getFullYear(),today.getMonth(),1);    //현재 달의 첫날
        var nm = new Date(today.getFullYear(),today.getMonth()+1,1);  //다음 달의 첫날
        var diff = dateDiff(nm,tm)       //한달 크기 구하기
        state.rcData.step =  dateDiff(nm,today)+1;            //다음 호봉 진급일

        if((nm.getTime()-tmp[4].getTime()) > 0 ){                      //다음 달 첫날이 전역 이후 일 때
          state.rcData.nmHouse= true;
        }else {
          state.rcData.nmHouse = false;
        }

        state.rcData.step_P = Math.round(((diff-state.rcData.step)/diff *100)*1000000)/1000000; // 다음 호봉 진급일 퍼센트
    }
  },
  actions: {
    login(dispatch, loginObj) {
    // login --> 토큰 반환
      axios
        .post(`${BACKEND_URL}/api/rest-auth/obtain_token/`, loginObj)
        // loginObj = {id,password}를 받아온다.
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
        // loginObj = {id,email,password1, password2}
        .then((res) => {
          alert('회원가입이 성공적으로 이뤄졌습니다.');
          router.push({ name: 'Login' });
          console.log(res);
        })
        .catch(() => {
          alert('뭔가 입력이 잘못됨.');
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