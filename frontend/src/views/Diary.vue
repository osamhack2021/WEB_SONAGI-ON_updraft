<template>
  <div>
    <v-card class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </v-card>
    <v-layout>
    <Timeline />
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
  import Timeline from '../components/Timeline'

  export default {
    name: 'Home',
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
             href: 'Diary',
           },
         ],
      diaryMonth: [
        '#August, 2020',
        '#November, 2020',
        '#May, 2021',
        '#October, 2021'
      ],
    }),

    components: {
      Timeline,
    },
  }
</script>

<style>
</style>