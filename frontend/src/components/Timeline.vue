<template>
<v-layout align-center justify-center row fill-height class="py-8 px-4">
  <v-card class="py-8 px-4 ma-4" style="max-width: 900px;">
      <div class="scroll-box">
        <v-timeline dense v-for="(v,k) in diaryData" :key="k">
          <a class="disablePointer ma-4" :name="k"></a>
          <div class="margin"></div>
          <v-card class="pa-2 ma-4" style="width: 150px; text-align: center;" color="blue-grey lighten-4">{{k}}</v-card>
          <v-timeline-item v-for="item in v" :key="item" :icon="'mdi-emoticon-'+item.emotion+'-outline'" :color="'#'+((Math.random()*0xFFFFFF<<0)%0xFFFFFF).toString(16)">
            <v-card class="pa-2 ma-2">
              <v-layout align-center justify-space-between row fill-height class="pa-2 ma-2">
              <v-card-title>{{item.title}}</v-card-title>
              <div>
                <v-btn depressed color="white" link :to="'/diary-write?id='+item.id"> 
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
                <v-btn depressed color="white" @click="deleteDiary(item.id)"> 
                  <v-icon>mdi-delete</v-icon>
                </v-btn>
              </div>
              
              </v-layout>
              <v-card class="pa-2 ma-2" :elevation="0">
              {{item.content}}
              </v-card>
              
              <div class="text-right">{{item.write_date}}</div>
            </v-card>
          </v-timeline-item>
        </v-timeline>
      </div>
  </v-card>
  
</v-layout>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  props: ['diaryData'],
  name: 'Timeline',
  data: () => ({
  }),
  computed: {
    ...mapState(['access_token']),
  },
  methods: {
    ...mapActions(['logout']),
    deleteDiary: function(id){
      this.$confirm("삭제 하시겠습니까? 되돌릴 수 없습니다.").then(() => {
        const config = {
          headers: {
            Authorization: `Bearer ${this.access_token}`,
          },
        };
        this.axios
          .post(`${this.$store.state.BACKEND_URL}/api/diary/delete`, {id}, config)
          .then(() => {
            this.$emit('reload');
            this.$alert("성공적으로 삭제되었습니다.","","success");
          })
          .catch(() => {
            this.logout();
            this.$alert("세션이 만료되었습니다. 다시 로그인 해주세요.","","error");
          });
      });
    }
  }
}
</script>

<style>
.disablePointer {
  pointer-events: none; 
}
.disablePointer:link {
  text-decoration: none;
  color: black;
}
.margin {
  margin-top: 100px;
}
</style>