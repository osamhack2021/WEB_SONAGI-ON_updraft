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
            <Emotions />
          </v-layout>
          <v-text-field
            v-model="message1"
            label="제목"
            clearable
          ></v-text-field>
          <v-textarea
          counter
          label="내용"
          :rules="rules"
          :value="value"
          rows="15"
          row-height="30"
          ></v-textarea>
        </v-card>
        <v-layout justify-center>
            <v-btn>
              작성하기
            </v-btn>
          </v-layout>
    </v-layout>
    </div>
</template>

<script>
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
    }),
    
}
</script>
<style lang="">
    
</style>