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
          <v-btn>
            작성하기
          </v-btn>
      </v-layout>
    </v-layout>
    </div>
</template>
<script>
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
    }),
    
}
</script>
<style>
    
</style>