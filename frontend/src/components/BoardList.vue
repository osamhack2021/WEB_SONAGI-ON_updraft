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

  export default {
    name: 'BoardList',
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
            {
              no: "3",
              title: "test3",
              name: '상병 정재훈',
              date: '2021/09/26'
            },
            {
              no: "4",
              title: "test4",
              name: '상병 정재훈',
              date: '2021/09/27'
            },
            {
              no: "5",
              title: "test5",
              name: '상병 정재훈',
              date: '2021/09/29'
            },
            {
              no: "6",
              title: "test6",
              name: '상병 정재훈',
              date: '2021/10/01'
            },
            {
              no: "7",
              title: "test7",
              name: '상병 정재훈',
              date: '2021/10/04'
            },
            {
              no: "8",
              title: "test8",
              name: '상병 정재훈',
              date: '2021/10/07'
            },
            {
              no: "9",
              title: "test9",
              name: '상병 정재훈',
              date: '2021/10/11'
            },
            {
              no: "10",
              title: "test10",
              name: '상병 정재훈',
              date: '2021/10/12'
            },
            {
              no: "11",
              title: "test11",
              name: '상병 정재훈',
              date: '2021/10/13'
            },
            {
              no: "12",
              title: "test12",
              name: '상병 정재훈',
              date: '2021/10/14'
            },
            {
              no: "13",
              title: "test13",
              name: '상병 정재훈',
              date: '2021/10/16'
            },
          ],
    }),
  }
</script>