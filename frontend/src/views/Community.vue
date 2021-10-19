<template>
    <div>
    <v-card class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </v-card>
    <v-layout justify-center>
    <v-card class="mt-4 pa-2" style="width: 900px;">
      <v-btn-toggle v-model="toggle_exclusive" mandantory>
      <v-row>
        <v-col class="col-3" align="center">
          <v-btn width="200px" @click="changeBoard(1)">
            <h2>자유 게시판</h2>
          </v-btn>
        </v-col>
        <v-col class="col-3" align="center">
          <v-btn width="200px" @click="changeBoard(2)">
            <h2>질문 게시판</h2>
          </v-btn>
        </v-col>
        <v-col class="col-3" align="center">
          <v-btn width="200px" @click="changeBoard(3)">
            <h2>정보 게시판</h2>
          </v-btn>
        </v-col>
        <v-col class="col-3" align="center">
          <v-btn width="200px" @click="changeBoard(4)">
            <h2>자랑 게시판</h2>
          </v-btn>
        </v-col>
      </v-row>
      </v-btn-toggle>
    </v-card>
    </v-layout>
    <template v-if="isLoaded">
      <BoardList :board_id="board_id" :key="board_id"/>
    </template>
    </div>
</template>

<script>
import BoardList from '../components/BoardList'

export default {
  components: {
    BoardList,
  },
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
    toggle_exclusive: undefined,
    board_id: 1,
    isLoaded: true,
  }),
  methods: {
    changeBoard: function(id){
      this.board_id = id;
      this.$forceUpdate();
    }
  },
  created(){
    if(this.$route.query.board_id !== undefined){
      this.board_id = this.$route.query.board_id;
    }
  }
}
</script>
<style>
    
</style>