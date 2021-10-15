<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="grey darken-2 white--text"
          dark
          v-bind="attrs"
          v-on="on"
        >
          회원가입
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">회원가입</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-form ref="registerform" lazy-validation>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  name="email"
                  label="이메일 *"
                  v-model="email"
                  :rules="emailRules"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  name="password"
                  label="패스워드 *"
                  v-model="password"
                  type="password"
                  :rules="passwordRules"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  name="password2"
                  label="패스워드 확인 *"
                  v-model="password2"
                  type="password"
                  :rules="passwordRules2"
                ></v-text-field>
              </v-col>
            </v-row>
            </v-form>
          </v-container>
          <small>* 필수 입력 항목입니다.</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="register({email, password, password2})"
          >
            확인
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
// https://minu0807.tistory.com/82
// https://sundries-in-myidea.tistory.com/130
// rule로 머 띄우는거 대해서 참고할 글 따봉

// https://vuetifyjs.com/en/components/alerts/#usage
// alert component를 써보자

export default {
  name: 'Register',
  // 아래와 같은 형식으로 data를 써야 안에서 this를 쓸 수 있다.
  data() {
    return {
      dialog: false,
      emailunique: true,
      email: "",
      emailRules: [
        v => !!v || '이메일은 필수 항목입니다.',
        v => /.+@.+\..+/.test(v) || '이메일 형식이 유효하지 않습니다.',
        v => v.length <= 30 || '이메일 길이는 최대 30자입니다.',
        () => this.emailunique || '이미 사용중인 이메일입니다.',
      ],
      password: "",
      passwordRules: [
        v => !!v || '패스워드는 필수 항목입니다.',
      ],
      password2: "",
      passwordRules2: [
        v => !!v || '패스워드 확인은 필수 항목입니다.',
        v => v === this.password || '패스워드가 일치하지 않습니다.',
      ],
    }
  },
  methods: {
    async register(signupObj){
      if (this.$refs.registerform.validate()){
        this.axios
          .post(`${this.$store.state.BACKEND_URL}/api/user/registration`, signupObj)
          .then(() => {
            this.dialog = false
            alert(`회원가입에 성공했습니다.\n설정에서 회원 정보를 변경하실 수 있습니다.`);
          })
          .catch((error) => {
            if(error.response.data.email){
              this.emailunique = false;
              this.$refs.registerform.validate();
            } else {
              alert('예상치 못한 문제가 발생했습니다.\n고객센터로 문의 바랍니다.');
            }
          });
      }
    },
  },
  watch: {
    dialog: function(val){
      if (!val){
        this.$refs.registerform.reset();
        this.emailunique = true;
      }
    },
    email: function() {
      this.emailunique = true;
    }
  }
}
</script>