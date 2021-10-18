<template>
    <div>
    <v-card class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </v-card>
    <v-layout align-center column fill-height class="py-8 px-4">
      <v-card class="py-8 px-4 ma-4" style="max-width: 900px; min-width: 900px; height: 700px">
        <v-form lazy-validation>
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
          <v-btn @click="writePost()">
            작성하기
          </v-btn>
      </v-layout>
    </v-layout>
    </div>
</template>


<script>
import {mapState} from 'vuex'
export default {
  data: ()=> ({
    bcLink: [
      {
        text: '대시보드',
        disabled: false,
        href: '/',
      },
      {
        text: '커뮤니티',
        disabled: false,
        href: 'community',
      },
    ],
    title: "",
    content: "",
    image: null,
  }),
  computed: {
    ...mapState(['isLogin', 'access_token']),
  },
  methods: {
    writePost: function(){
      const config = {
        headers: {
          Authorization: `Bearer ${this.access_token}`,
        },
      };
      const postObject = {
        "board_id":this.$route.query.board_id,
        "title":this.title,
        "content":this.content,
        "image":this.image,
      }
      this.axios
      .post(`${this.$store.state.BACKEND_URL}/api/community/post/write`, postObject, config)
      .then(() => {
        this.$router.push("/community?board_id="+this.$route.query.board_id)
        this.$alert("게시글 작성에 성공했습니다.","","success");
      })
      .catch(() => {
        this.$alert("세션이 만료되었습니다. 다시 로그인 해주세요.","","error");
      });
    }
  },
  created() {
    if(!this.isLogin){
      this.$alert("로그인이 필요한 페이지입니다.", "", "warning");
      this.$router.push("/");
      return;
    }
  },
}
</script>
<style>
    
</style>