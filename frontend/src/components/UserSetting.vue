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
          설정
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">설정</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-form ref="usersettingform" lazy-validation>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  name="email"
                  label="이메일"
                  v-model="email"
                  readonly
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  name="password"
                  label="패스워드"
                  v-model="password"
                  type="password"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  name="password2"
                  label="패스워드 확인"
                  v-model="password2"
                  type="password"
                  :rules="passwordRules2"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  name="nickname"
                  label="닉네임"
                  v-model="nickname"
                  :rules="nicknameRules"
                ></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-select
                  v-model="major"
                  :items="major_items"
                  item-text="state"
                  item-value="abbr"
                  hint="군 구분"
                  persistent-hint
                  return-object
                  single-line
                ></v-select>
              </v-col>
              <v-col cols="6">
                <v-select
                  v-model="type"
                  :items="type_items"
                  item-text="state"
                  item-value="abbr"
                  hint="복무 형태"
                  persistent-hint
                  return-object
                  single-line
                ></v-select>
              </v-col>
              <v-col cols="6">
                <UserSettingDatePicker
                  type='enlisted_date'
                  label='입대일'
                  v-bind:propDate="enlisted_date" 
                  @date-extract="updateDate"
                ></UserSettingDatePicker>
              </v-col>
              <v-col cols="6">
                <UserSettingDatePicker
                  type='delisted_date'
                  label='전역일'
                  v-bind:propDate="delisted_date" 
                  @date-extract="updateDate"
                ></UserSettingDatePicker>
              </v-col>
              <v-col cols="4">
                <UserSettingDatePicker
                  type='promotion1_date'
                  v-bind:label='promotion1_label'
                  v-bind:propDate="promotion1_date" 
                  @date-extract="updateDate"
                ></UserSettingDatePicker>
              </v-col>
              <v-col cols="4">
                <UserSettingDatePicker
                  type='promotion2_date'
                  v-bind:label='promotion2_label'
                  v-bind:propDate="promotion2_date" 
                  @date-extract="updateDate"
                ></UserSettingDatePicker>
              </v-col>
              <v-col cols="4">
                <UserSettingDatePicker
                  type='promotion3_date'
                  v-bind:label='promotion3_label'
                  v-bind:propDate="promotion3_date" 
                  @date-extract="updateDate"
                ></UserSettingDatePicker>
              </v-col>
            </v-row>
            </v-form>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="updateSetting()"
          >
            변경
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import UserSettingDatePicker from './UserSettingDatePicker.vue'

export default {
  name: 'UserSetting',
  components: {
    UserSettingDatePicker,
  },
  // 아래와 같은 형식으로 data를 써야 안에서 this를 쓸 수 있다.
  data() {
    return {
      dialog: false,
      email: "",
      password: "",
      password2: "",
      passwordRules2: [
        v => v === this.password || '패스워드가 일치하지 않습니다.',
      ],
      nickname: "",
      nicknameRules: [
        v => v.length > 1 || '닉네임은 2자 이상이어야 합니다.',
        v => v.length < 16 || '닉네임은 15자 이하여야 합니다.',
      ],
      major: { state: '', abbr: '' },
      major_items: [
        { state: '육군', abbr: 'army' },
        { state: '해군', abbr: 'navy' },
        { state: '공군', abbr: 'air' },
        { state: '해병대', abbr: 'marine' },
      ],
      type: { state: '', abbr: '' },
      type_items: [
        { state: '용사', abbr: 'soldier' },
        { state: '부사관', abbr: 'nco' },
        { state: '장교', abbr: 'officer' },
      ],
      enlisted_date: "2021-10-14",
      delisted_date: "2021-10-18",
      promotion1_label : "일병 진급일",
      promotion1_date: "2021-10-15",
      promotion2_label : "상병 진급일",
      promotion2_date: "2021-10-16",
      promotion3_label : "병장 진급일",
      promotion3_date: "2021-10-17",
    }
  },
  computed: {
    ...mapState(['isLogin', 'access_token', 'refresh_token', 'userdata']),
  },
  methods: {
    ...mapActions(['updateUserdata']),
    refreshInfo: function(){
      this.email = this.userdata.email;
      this.nickname = this.userdata.nickname;
      this.major = this.major_items.filter(v => v.abbr === this.userdata.major)[0];
      this.type = this.type_items.filter(v => v.abbr === this.userdata.type)[0];
      this.enlisted_date = this.userdata.enlisted_date;
      this.delisted_date = this.userdata.delisted_date;
      this.promotion1_date = this.userdata.promotion1_date ;
      this.promotion2_date = this.userdata.promotion2_date;
      this.promotion3_date = this.userdata.promotion3_date
    },
    updateSetting: function(){
      const config = {
        headers: {
          Authorization: `Bearer ${this.access_token}`,
        },
      };
      const updateObj = {"nickname":this.nickname,
                         "major":this.major.abbr,
                         "type":this.type.abbr,
                         "enlisted_date":this.enlisted_date,
                         "delisted_date":this.delisted_date,
                         "promotion1_date":this.promotion1_date,
                         "promotion2_date":this.promotion2_date,
                         "promotion3_date":this.promotion3_date,}
      this.axios.post(`${this.$store.state.BACKEND_URL}/api/usersetting/revise`, updateObj, config)
        .then(() => {
          this.updateUserdata();
          alert("성공적으로 변경되었습니다.");
        })
        .catch(() => {
          this.updateUserdata();
        })
    },
    updateDate: function({type, newDate}){
      this[type] = newDate;
    }
  },
  watch: {
    dialog: function(val){
      if (val){
        this.refreshInfo();
      }
    },
  }
}
</script>