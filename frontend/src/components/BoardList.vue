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
            :sort-by="['id']"
            :sort-desc="[true]"
          > 
          <template #item.title="{ item }">
            <router-link :to="{ name: '커뮤니티 게시글', query: { board_id: board_id, post_id: item.id } }"
              style="text-decoration: none; color: inherit;"
            >
              {{ item.title }}
            </router-link>
          </template>
          </v-data-table>
          <v-row justify="center" class="pa-4">
            <v-btn link :to="'/community-write?board_id='+this.board_id">
              글쓰기
            </v-btn>
          </v-row>
        </v-card>
      </v-layout>
</template>

<script>
import {mapState} from 'vuex'

export default {
  props: ['board_id'],
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
        value: 'id',
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
        value: 'nickname',
        width: 130,
      },
      { 
        text: '작성일자', 
        align: 'center',
        sortable: false,
        value: 'write_date', 
        width: 120,
      },
    ],
    bdList: [
    ],
  }),
  methods: {
    updateBoard: function(){
      const config = {
        headers: {
          Authorization: `Bearer ${this.access_token}`,
        },
      };
      this.axios
      .post(`${this.$store.state.BACKEND_URL}/api/community/post/list`, {'board_id':this.board_id}, config)
      .then((res) => {
        this.bdList = res.data;
        for (let i = 0; i < this.bdList.length; i++){
          this.bdList[i].write_date = this.bdList[i].write_date.split('T')[0];
        }
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
    } else{
      this.updateBoard();
    }
  },
}
</script>