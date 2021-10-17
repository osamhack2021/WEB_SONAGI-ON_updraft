<template>
  <div>
    <v-card class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </v-card>
    <v-layout>
    <Timeline
      v-if="isLoaded"
      :diaryData="diaryData"
      @reload="initTimeline"
    >
    </Timeline>
    <v-flex xs2 sm2 md2 lg2 xl2 shrink>
    <v-card class="mt-10" style="position: fixed;">
      <v-subheader class="grey darken-3 white--text" style="text-align: center;">Quick List</v-subheader>
      <v-list>    
        <v-list-item v-for="item in diaryMonth" :key="item" v-bind:href=item style="text-align: center;">{{item.slice(1)}}
        </v-list-item>
      </v-list>
    </v-card>
    </v-flex>
    </v-layout>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import Timeline from '../components/Timeline'

export default {
  name: 'Home',
  components: {
    Timeline
  },
  data: ()=> ({
    bcLink: [
          {
            text: '대시보드',
            disabled: false,
            href: '/',
          },
          {
            text: '일기',
            disabled: false,
            href: 'Diary',
          },
        ],
    diaryMonth: [],
    diaryData: {},
    isLoaded: false,
  }),
  computed: {
    ...mapState(['isLogin', 'access_token']),
  },
  methods: {
    ...mapActions(['logout']),
    initTimeline: function(){
      this.diaryMonth = [];
      this.diaryData = {};
      this.isLoaded = false;
      if(!this.isLogin){
        this.$alert("로그인이 필요한 페이지입니다.","","warning");
        this.$router.push('/');
      } else {
        const config = {
          headers: {
            Authorization: `Bearer ${this.access_token}`,
          },
        };
        this.axios
          .get(`${this.$store.state.BACKEND_URL}/api/diary/list`, config)
          .then((res) => {
            let monthyear = [];
            let sorted_data = res.data.sort((a,b) => {
              a = new Date(a.write_date);
              b = new Date(b.write_date);
              return a < b ? 1 : -1;
            })
            for(let i = 0; i < sorted_data.length; i++){
              let tmp = sorted_data[i]['write_date'].split('-');
              tmp = tmp[0] + ", " + tmp[1] + "월";
              if (tmp in this.diaryData){
                this.diaryData[tmp].push(sorted_data[i]);
              } else {
                this.diaryData[tmp] = [sorted_data[i]];
                tmp = "#"+tmp;
                monthyear.push(tmp);
              }
            }
            this.diaryMonth = monthyear;
            this.isLoaded = true;
          })
          .catch(() => {
            this.logout();
            this.$alert("세션이 만료되었습니다. 다시 로그인 해주세요.","","error");
          });
      }
    }
  },
  created() {
    this.initTimeline();
  },
}
</script>

<style>
</style>