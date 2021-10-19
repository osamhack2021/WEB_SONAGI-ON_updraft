<template>
    <div>
        <v-card class="group pa-2">
        <v-icon small style="margin-left:5px">home</v-icon>
        <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
        </v-card>
        <v-layout justify-center>
        <v-card class="pa-4 ma-4" style="width: 900px;">
            <v-card tile class="elevation-0">
                <v-toolbar flat color="grey lighten-3"><h2>{{postData.title}}</h2></v-toolbar>
                <v-divider></v-divider>
                <v-row>
                    <v-col class="ma-2"><h4>작성자</h4> : {{postData.nickname}}</v-col>
                    <v-col class="ma-2" align="right">
                        <h4>작성일</h4> : {{postData.write_date}}   <h4>조회수</h4> : {{Math.floor(Math.random() * 100)}}
                    </v-col>
                </v-row>
                <v-divider></v-divider>
                <v-card tile class="elevation-0 ma-2" style="min-height: 300px;">
                    {{postData.content}}
                </v-card>
                <div class="ma-2">
                    <v-row>
                        <v-col>
                            <h4>댓글</h4> {{comments.length}}
                        </v-col>
                        <v-col align="right">
                            <v-btn link to="/community"><h4>목록</h4></v-btn>
                        </v-col>
                    </v-row>
                </div>
                <v-divider></v-divider>
                <div>
                    <v-card tile class="elevation-0 ma-4" style="min-height: 100px;">
                        <v-row class="mt-2">
                            <v-textarea
                            solo
                            auto-grow
                            nickname="comments"
                            v-model="comment.content"
                            label="댓글을 입력하세요."
                            background-color="grey lighten-3"
                            rows="4"
                            ></v-textarea>
                        </v-row>
                        <v-row>
                            <v-col align="right">
                                <v-btn @click="writeComment()">댓글 작성</v-btn>
                            </v-col>
                        </v-row>
                    </v-card>
                    <v-divider></v-divider>
                </div>
                <div v-for="(v, k) in comments" :key="k">
                    <v-card tile class="elevation-0 ma-4" style="min-height: 100px;">
                        <v-row>
                            <v-col class="mt-2 col-1 primary--text">{{v.class}} {{v.nickname}}</v-col>
                            <v-col class="mt-2 col-3 grey--text" align="left">
                                {{v.write_date.split('T')[0] + " " + v.write_date.split('T')[1].split(".")[0]}}
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col class="mb-3 ml-3">{{v.content}}</v-col>
                        </v-row>
                    </v-card>
                    <v-divider></v-divider>
                </div>
                <v-divider></v-divider>
                <v-row>
                    <v-col class="col-2">
                        <v-card flat class="pa-2" color="grey lighten-3" align="center">
                            <h4>이전 글</h4>
                        </v-card>
                    </v-col>
                    <v-col class="my-2">
                      <router-link :to="{ name: '커뮤니티 게시글', query: { board_id: board_id, post_id: prevpostData.id } }"
                        style="text-decoration: none; color: inherit;"
                      >
                        {{prevpostData.title}}
                      </router-link>
                    </v-col>
                    <v-col class="ma-2" align="right">{{prevpostData.write_date}}</v-col>
                </v-row><v-divider></v-divider>
                <v-row>
                    <v-col class="col-2">
                        <v-card flat class="pa-2" color="grey lighten-3" align="center">
                            <h4>다음 글</h4>
                        </v-card>
                    </v-col>
                    <v-col class="my-2">
                      <router-link :to="{ name: '커뮤니티 게시글', query: { board_id: board_id, post_id: nextpostData.id } }"
                        style="text-decoration: none; color: inherit;"
                      >
                        {{nextpostData.title}}
                      </router-link>
                    </v-col>
                    <v-col class="ma-2" align="right">{{nextpostData.write_date}}</v-col>
                </v-row>
                <v-divider></v-divider>
            </v-card>
        </v-card>
        </v-layout>
    </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  nickname: 'Post',
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
    board_id: null,
    post_id: null,
    postData:{
      title: "",
      nickname: "",
      write_date: "",
      content: "",
    },
    prevpostData:{
      id: null,
      title: "",
      write_date: "",
    },
    nextpostData:{
      id: null,
      title: "",
      write_date: "",
    },
    comments: [
      {
        class: "",
        nickname: "",
        write_date: "",
        content: "",
      },
    ],
    comment: {
      content:"",
    }
  }),
  computed: {
    ...mapState(['isLogin', 'access_token']),
  },
  methods: {
    updatePost: function() {
      const config = {
        headers: {
          Authorization: `Bearer ${this.access_token}`,
        },
      };
      this.axios
        .post(`${this.$store.state.BACKEND_URL}/api/community/post/show`, {'id':this.post_id}, config)
        .then((res) => {
          this.postData = res.data;
          let tmp = this.postData.write_date;
          tmp = tmp.split(".")[0];
          this.postData.write_date = tmp.split("T")[0] + " " + tmp.split("T")[1];
          if(this.postData.prev_id !== null){
            this.updatePrev(this.postData.prev_id);
          }
          if(this.postData.next_id !== null){
            this.updateNext(this.postData.next_id);
          }
        })
        .catch(() => {
          this.$alert("세션이 만료되었습니다. 다시 로그인 해주세요.","","error");
        });
    },
    updateComment: function() {
      const config = {
          headers: {
            Authorization: `Bearer ${this.access_token}`,
        },
      };
      this.axios
        .post(`${this.$store.state.BACKEND_URL}/api/community/comment/list`, {'post_id':this.post_id}, config)
        .then((res) => {
          this.comments = res.data;
        })
        .catch(() => {
          this.$alert("세션이 만료되었습니다. 다시 로그인 해주세요.","","error");
        });
    },
    updatePrev: function(id){
      const config = {
        headers: {
          Authorization: `Bearer ${this.access_token}`,
        },
      };
      this.axios
        .post(`${this.$store.state.BACKEND_URL}/api/community/post/show`, {'id':id}, config)
        .then((res) => {
          this.prevpostData = res.data;
          let tmp = this.prevpostData.write_date;
          this.prevpostData.write_date = tmp.split("T")[0];
        })
        .catch(() => {
          this.$alert("세션이 만료되었습니다. 다시 로그인 해주세요.","","error");
        });
    },
    updateNext: function(id){
      const config = {
        headers: {
          Authorization: `Bearer ${this.access_token}`,
        },
      };
      this.axios
        .post(`${this.$store.state.BACKEND_URL}/api/community/post/show`, {'id':id}, config)
        .then((res) => {
          this.nextpostData = res.data;
          let tmp = this.nextpostData.write_date;
          this.nextpostData.write_date = tmp.split("T")[0];
        })
        .catch(() => {
          this.$alert("세션이 만료되었습니다. 다시 로그인 해주세요.","","error");
        });
    },
    writeComment: function() {
      const config = {
          headers: {
            Authorization: `Bearer ${this.access_token}`,
        },
      };
      this.axios
        .post(`${this.$store.state.BACKEND_URL}/api/community/comment/write`, {'post_id':this.post_id,"content":this.comment.content}, config)
        .then(() => {
          this.updateComment();
        })
        .catch(() => {
          this.$alert("세션이 만료되었습니다. 다시 로그인 해주세요.","","error");
        });
    },
  },
  created() {
    if(!this.isLogin){
      this.$alert("로그인이 필요한 페이지입니다.", "", "warning");
      this.$router.push("/");
      return;
    } else{
      this.board_id = this.$route.query.board_id;
      this.post_id = this.$route.query.post_id;
      this.updatePost();
      this.updateComment();
    }
  },
  watch: {
    $route: function(){
        if(!this.isLogin){
        this.$alert("로그인이 필요한 페이지입니다.", "", "warning");
        this.$router.push("/");
        return;
      } else{
        this.prevpostData = {};
        this.nextpostData = {};
        this.board_id = this.$route.query.board_id;
        this.post_id = this.$route.query.post_id;
        this.updatePost();
        this.updateComment();
      }
    }
  },
}
</script>

<style>
    h4 {display: inline;}
</style>