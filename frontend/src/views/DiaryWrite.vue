<template lang="">
    <div class="pb-8">
    <v-card class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </v-card>
    <v-layout align-center column fill-height class="py-8 px-4">
      <v-card class="py-8 px-4 ma-4" style="max-width: 900px; width: 900px; height: 700px">
        <v-card-title class="justify-center">
          오늘 나의 감정
        </v-card-title>
        <v-layout justify-center>
          <Emotions
            @emotion-extract="updateEmotion"
          > </Emotions>
        </v-layout>
        <v-form ref="diaryform" lazy-validation>
          <v-text-field
            v-model="title"
            label="제목"
            :rules="titleRules"
            clearable
          ></v-text-field>
          <v-textarea
          counter
          v-model="content"
          label="내용"
          :rules="contentRules"
          rows="15"
          row-height="30"
          ></v-textarea>
        </v-form>
      </v-card>
      <v-layout justify-center>
          <v-btn @click="diaryWrite({title, content, emotion})">
            작성하기
          </v-btn>
      </v-layout>
    </v-layout>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import Emotions from '../components/Emotions'

export default {
  components: {
    Emotions,
  },
  data: ()=> ({
    bcLink: [
      {
        text: '대시보드',
        disabled: false,
        href: 'Dashboard',
      },
      {
        text: '일기',
        disabled: false,
        href: 'diary',
      },
      {
        text: '일기 쓰기',
        disabled: false,
        href: 'diary-write',
      },
    ],
    emotion: "",
    title: "",
    titleRules: [
      v => !!v || '제목은 필수 항목입니다.',
      v => v.length < 25 || '제목은 25자 이하로 적어주세요.'
    ],
    content: "",
    contentRules: [
      v => !!v || '내용은 필수 항목입니다.',
      v => v.length < 1500 || '내용은 1500자 이하로 적어주세요.'
    ],
  }),
  computed: {
    ...mapState(['isLogin', 'access_token']),
  },
  methods: {
    ...mapActions(['logout']),
    updateEmotion: function(emotion){
      this.emotion = emotion;
    },
    diaryWrite: function(diaryObj) {
      if(!this.isLogin){
        alert('로그인이 필요합니다.');
        return;
      }
      const is_valid = this.$refs.diaryform.validate();
      if(is_valid){
        const config = {
          headers: {
            Authorization: `Bearer ${this.access_token}`,
          },
        };
        this.axios
          .post(`${this.$store.state.BACKEND_URL}/api/diary/write`, diaryObj, config)
          .then(() => {
            alert(`일기 작성에 성공했습니다.`);
            this.$refs.diaryform.reset();
          })
          .catch(() => {
            this.logout();
            alert("세션이 만료되었습니다. 다시 로그인 해주세요.");
          });
      }
    }
  },
}
</script>
<style lang="">
    
</style>