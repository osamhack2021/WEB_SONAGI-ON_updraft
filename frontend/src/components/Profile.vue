<template>
   <v-card height="350px" class="d-flex align-center justify-center">
      <v-list>
         <v-list-item>
            <v-icon size=150>mdi-account-circle</v-icon>
         </v-list-item>
         <v-list-item link>
            <v-list-item-content>
               <v-list-item-title class="text-h5 d-flex align-center justify-center">{{nickname}}</v-list-item-title>
               <v-list-item-subtitle class="d-flex align-center justify-center">{{rank}}</v-list-item-subtitle>
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
               <v-btn
                  color="grey darken-2 white--text"
                  dark
                  @click="logout()"
               > 
                  로그아웃
               </v-btn>
            </template>
         </v-list-item>
      </v-list>
   </v-card>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import LoginDialog from './LoginDialog.vue'
import Register from './Register.vue'

export default {
  name: 'Profile',
  components: { 
    LoginDialog,
    Register,
  },
  data: () => ({
     nickname: "무명",
     rank: "게스트",
  }),
  computed: {
    ...mapState(['isLogin']),
  },
  methods: {
     ...mapActions(['logout']),
  },
}
</script>