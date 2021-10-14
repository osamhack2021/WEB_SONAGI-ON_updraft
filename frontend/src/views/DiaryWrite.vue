<template lang="">
    <div>
    <v-card class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </v-card>
    <v-layout align-center justify-center row fill-height class="py-8 px-4">
        <v-card class="py-8 px-4 ma-4" style="max-width: 900px; width: 900px; height: 700px">
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