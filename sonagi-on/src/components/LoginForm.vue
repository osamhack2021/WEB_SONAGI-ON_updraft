<template>
   <v-app id="inspire">
      <v-main>
         <v-container fluid fill-height>
            <v-layout align-center justify-center>
               <v-flex xs12 sm8 md4>
                  <v-card class="elevation-12">
                     <v-toolbar dark color="primary">
                        <v-toolbar-title>로그인</v-toolbar-title>
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
                              id="password"
                              prepend-icon="lock"
                              v-model="password"
                              label="패스워드"
                              type="password"
                           ></v-text-field>
                        </v-form>
                     </v-card-text>
                     <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" @click="login({username, password})">Login</v-btn>
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
  name: 'LoginForm',
  data: () => ({
    username: null,
    password: null,
  }),
  computed: {
    ...mapState(['isLogin', 'isLoginError']),
  },
  methods: {
    ...mapActions(['login']),
  },
});
</script>
