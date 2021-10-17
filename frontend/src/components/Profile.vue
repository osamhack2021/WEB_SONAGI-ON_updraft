<template>
   <v-card height="350px" class="d-flex align-center justify-center">
      <v-list>
        <v-list-item>
          <template v-if="!isLogin">
                <v-icon size=150>mdi-account-circle</v-icon>
          </template>
          <template v-else>
            <v-avatar size="150">
              <img
                :src="$store.state.BACKEND_URL+'/'+user.profile"
                alt="에러"
              >
            </v-avatar>
          </template>
        </v-list-item>
         <v-list-item>
            <v-list-item-content>
               <v-list-item-title class="text-h5 d-flex align-center justify-center">{{user.nickname}}</v-list-item-title>
               <v-list-item-subtitle class="d-flex align-center justify-center">{{user.rank}}</v-list-item-subtitle>
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
    user: {"nickname":"무명", "rank":"게스트", "profile":null},
  }),
  computed: {
    ...mapState(['isLogin', 'userdata']),
  },
  methods: {
    ...mapActions(['logout']),
    initProfile: function() {
      if(this.isLogin){
        this.user.nickname = this.userdata.nickname;
        this.user.profile = this.userdata.profile;
        let promotion_dates = [new Date(this.userdata.promotion1_date), 
                                new Date(this.userdata.promotion2_date), 
                                new Date(this.userdata.promotion3_date)];
        let today = new Date();
        // todo : 부사관, 장교에 대해서도 나타낼 수 있도록
        if(this.userdata.type === "soldier"){
          let ranks = ["이병", "일병", "상병", "병장"];
          for(let i = 0; i < promotion_dates.length; i++){
            if(today < promotion_dates[i]){
              this.user.rank = ranks[i]
              break;
            }
          }
        }
      } else {
        this.user = {"nickname":"무명", "rank":"게스트"};
      }
    },
  },
  watch: {
    userdata: function() {
      this.initProfile();
    },
  },
  created() {
    this.initProfile();
  },
}
</script>