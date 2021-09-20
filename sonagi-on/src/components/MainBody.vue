<template>
   <v-app>
      <v-main>
         <v-container fluid fill-height>
            <v-layout align-top justify-center>
               <v-flex xs12 sm8 md4 class="text-center">
                  <v-card class="elevation-12">
                     <v-card-text v-if="!isLogin">
                        로그인이 필요합니다.
                     </v-card-text>
                     <v-card-text v-else>
                        환영합니다 {{ userInfo.username }}님.
                     </v-card-text>
                     <v-card-actions class="justify-center">
                        <template v-if="!isLogin">
                           <v-btn to="/login" elevation="2" color="primary">
                              로그인
                           </v-btn>
                           <v-btn elevation="2" color="primary">
                              회원가입
                           </v-btn>
                        </template>
                        <template v-else>
                           <v-btn @click="logout()" elevation="2" color="primary">
                              로그아웃
                           </v-btn>
                        </template>
                     </v-card-actions>
                  </v-card>
               </v-flex>
            </v-layout>
         </v-container>
      </v-main>
   </v-app>
</template>

<script lang="ts">
import { mapState, mapActions } from 'vuex';
import Vue from 'vue';

export default Vue.extend({
  name: 'MainBody',

  data: () => ({
  }),

  computed: {
    ...mapState(['isLogin', 'userInfo']),
  },
  methods: {
    ...mapActions(['logout']),
  },
});
</script>
