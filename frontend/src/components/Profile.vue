<template>
   <v-card height="350px" class="d-flex align-center justify-center">
      <v-list>
         <v-list-item>
            <v-icon size=150>mdi-account-circle</v-icon>
         </v-list-item>
         <v-list-item>
            <v-list-item-content>
               <v-list-item-title class="text-h5 d-flex align-center justify-center">{{userdata.nickname}}</v-list-item-title>
               <v-list-item-subtitle class="d-flex align-center justify-center">{{userdata.rank}}</v-list-item-subtitle>
            </v-list-item-content>
         </v-list-item>
         <v-list-item class="justify-center">
            <template v-if="!isLogin">
                <v-row>
                  <v-col>
                    <LoginDialog />
                  </v-col>
                  <v-col>
                    <Register />
                  </v-col>
                </v-row>
            </template>
            <template v-else>
              <v-row>
                  <v-col>
                    <UserSetting />
                  </v-col>
                  <v-col>
                    <v-row justify="center">
                      <v-btn
                          color="grey darken-2 white--text"
                          dark
                          @click="logout()"
                      > 
                          로그아웃
                      </v-btn>
                    </v-row>
                  </v-col>
               </v-row>
            </template>
         </v-list-item>
      </v-list>
   </v-card>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import LoginDialog from './LoginDialog.vue'
import Register from './Register.vue'
import UserSetting from './UserSetting.vue'

export default {
  name: 'Profile',
  components: { 
    LoginDialog,
    Register,
    UserSetting,
  },
  data: () => ({
    userdata: {"nickname":"무명", "rank":"게스트"},
  }),
  computed: {
    ...mapState(['isLogin', 'access_token', 'refresh_token']),
  },
  methods: {
     ...mapActions(['logout']),
     initProfile: function() {
       if(this.isLogin){
        const config = {
          headers: {
            Authorization: `Bearer ${this.access_token}`,
          },
        };
        this.axios.get(`${this.$store.state.BACKEND_URL}/api/usersetting/get`, config)
          .then((res) => {
            this.userdata.nickname = res.data.nickname;
            let promotion_dates = [new Date(res.data.promotion1_date), 
                                   new Date(res.data.promotion2_date), 
                                   new Date(res.data.promotion3_date)];
            let today = new Date();
            // todo : 부사관, 장교에 대해서도 나타낼 수 있도록
            if(res.data.type === "soldier"){
              let ranks = ["이병", "일병", "상병", "병장"];
              for(let i = 0; i < promotion_dates.length; i++){
                console.log(today, promotion_dates[i]);
                if(today < promotion_dates[i]){
                  this.userdata.rank = ranks[i]
                  break;
                }
              }
            }
          })
          .catch((error) => {
            if(error.response.data.code === "token_not_valid"){
              this.logout();
              alert("세션이 만료되었습니다. 다시 로그인 해주세요.");
            } else {
              this.logout();
              alert("[PF001] 예상치 못한 에러가 발생했습니다.")
            }
          })
      } else {
        this.userdata = {"nickname":"무명", "rank":"게스트"};
      }
     },
  },
  watch: {
    isLogin: function() {
      this.initProfile();
    }
  },
  created() {
    this.initProfile();
  }
}
</script>