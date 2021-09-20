<template>
   <v-app>
      <v-main>
         <v-container fluid fill-height>
            <v-layout align-center justify-center>
               <v-flex xs12 sm8 md4>
                  <v-card class="elevation-12">
                     <v-toolbar dark color="primary">
                        <v-toolbar-title>회원가입</v-toolbar-title>
                     </v-toolbar>
                     <v-card-text>
                        <v-form>
                           <v-text-field
                              prepend-icon="person"
                              v-model="username"
                              label="아이디"
                              type="text"
                           ></v-text-field>
                           <v-text-field
                              prepend-icon="mail"
                              v-model="email"
                              label="이메일"
                              type="text"
                           ></v-text-field>
                           <v-text-field
                              prepend-icon="face"
                              v-model="nickname"
                              label="닉네임"
                              type="text"
                           ></v-text-field>
                           <v-text-field
                              id="password1"
                              prepend-icon="lock"
                              v-model="password1"
                              label="패스워드"
                              type="password"
                           ></v-text-field>
                           <v-text-field
                              id="password2"
                              prepend-icon="lock"
                              v-model="password2"
                              label="패스워드 확인"
                              type="password"
                           ></v-text-field>
                        </v-form>
                     </v-card-text>
                     <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" @click="signup({username, email, password1, password2})">회원가입</v-btn>
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
  name: 'SignupForm',
  data: () => ({
    username: null,
    email: null,
    nickname: null,
    password1: null,
    password2: null,
  }),
  computed: {
    ...mapState(['isLogin', 'isLoginError']),
  },
  methods: {
    ...mapActions(['signup']),
  },
});
</script>
