<template>
    <div>
    <v-card class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </v-card>
    <BoardList />
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
      
    }),
    
}
</script>
<style>
    
</style>