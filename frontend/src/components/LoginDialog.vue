<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      max-width="600px"
      @click:outside="closeDialog"
    > 
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="grey darken-2 white--text"
          dark
          v-bind="attrs"
          v-on="on"
        > 
          로그인
        </v-btn>
      </template>
                  <v-card class="elevation-12">
                     <v-toolbar dark color="grey darken-2 white--text">
                        <v-toolbar-title>Login</v-toolbar-title>
                     </v-toolbar>
                     <v-alert
                      type="error"
                      v-model="loginerror"
                    > 존재하지 않는 계정입니다. </v-alert>
                     <v-card-text>
                        <v-form ref="loginform" lazy-validate>
                           <v-text-field
                              prepend-icon="mail"
                              name="login"
                              label="Email"
                              v-model="email"
                              :rules="emailRules"
                           ></v-text-field>
                           <v-text-field
                              id="password"
                              prepend-icon="lock"
                              name="password"
                              v-model="password"
                              label="Password"
                              type="password"
                              :rules="passwordRules"
                           ></v-text-field>
                        </v-form>
                     </v-card-text>
                     <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" @click="clicklogin({email, password})">Login</v-btn>
                     </v-card-actions>
                  </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import {  mapActions } from 'vuex';

export default {
  name: 'Login',
  props: {
    source: String,
  },
  data: () => ({
    email: null,
    emailRules: [
      v => !!v || '이메일은 필수 항목입니다.',
      v => /.+@.+\..+/.test(v) || '이메일 형식이 유효하지 않습니다.',
    ],
    password: null,
    passwordRules: [
      v => !!v || '패스워드는 필수 항목입니다.',
    ],
    dialog: false,
    loginerror: false,
  }),
  methods: {
    ...mapActions(['login']),
    clicklogin(loginobj) {
      const is_valid = this.$refs.loginform.validate();
      if (is_valid){
        this.login(loginobj)
          .catch(() => {
            this.loginerror = true;
          })
      }
    },
    closeDialog() {
      this.$refs.loginform.reset();
      this.loginerror = false;
    },
  },
};
</script>

<style></style>