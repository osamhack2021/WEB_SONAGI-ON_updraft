<template>
      <v-layout justify-center ma-4 pa-4>
        <v-card style="width: 900px;" class="elevation-4 pa-2 ma-2">
          <v-card-title>
            목록
            <v-spacer></v-spacer>
            <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="bdList"
            :search="search"
            :sort-by="['no']"
            :sort-desc="[true]"
          ></v-data-table>
          <v-row justify="center" class="pa-4">
            <v-btn link to="/community-write">
              글쓰기
            </v-btn>
          </v-row>
        </v-card>
      </v-layout>
</template>

<script>
import {mapState} from 'vuex'

export default {
  props: ['boardid'],
  name: 'BoardList',
  computed: {
    ...mapState(['isLogin', 'access_token']),
  },
  data: ()=>({
    search: '',
    headers: [
      {
        text: 'No',
        align: 'center',
        sortable: true,
        value: 'no',
        width: 30,
      },
      { 
        text: '제목', 
        align: 'start',
        sortable: false,
        value: 'title'
      },
      { 
        text: '작성자', 
        align: 'center',
        sortable: false,
        value: 'name',
        width: 130,
      },
      { 
        text: '날짜', 
        align: 'center',
        sortable: false,
        value: 'date', 
        width: 60,
      },
    ],
    bdList: [
      {
        no: "1",
        title: "[공지]게시판 이용 가이드",
        name: '관리자',
        date: '2021/09/22'
      },
      {
        no: "2",
        title: "아 전역 언제하냐",
        name: '상병 정재훈',
        date: '2021/09/24'
      },
    ],
  }),
  mehotds: {
    
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