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
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="이메일 *"
                  v-model="email"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="패스워드 *"
                  v-model="password"
                  type="password"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="패스워드 확인 *"
                  v-model="password2"
                  type="password"
                  required
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
              >
                <v-select
                  :items="['0-17', '18-29', '30-54', '54+']"
                  label="Age*"
                  required
                ></v-select>
              </v-col>
              <v-col
                cols="12"
                sm="6"
              >
                <v-autocomplete
                  :items="['Skiing', 'Ice hockey', 'Soccer', 'Basketball', 'Hockey', 'Reading', 'Writing', 'Coding', 'Basejump']"
                  label="Interests"
                  multiple
                ></v-autocomplete>
              </v-col>
            </v-row>
          </v-container>
          <small>* 필수 입력 칸입니다.</small>
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
  data: () => ({
    dialog: false,
    email: "",
    password: "",
    password2: "",
  }),
  methods: {
    register(signupObj){
      this.axios
        .post(`${this.$store.state.BACKEND_URL}/api/user/registration`, signupObj)
        .then(() => {
          alert(`회원가입이 성공적으로 이뤄졌습니다.\n회원 정보 수정에서 복무 정보를 입력하실 수 있습니다.`);
        })
        .catch(() => {
          // todo : 응답에 맞게 alert 띄우기
          // todo : signup은 Register.vue에 넣자. 왜? -> 잘못된 입력에 대해서 응답으로 온 에러를 alert 말고 입력칸 위에 빨갛게 띄워주는게 나을듯. 어차피 commit도 안함.
          alert('에러');
        });
    }
  }
}
</script>