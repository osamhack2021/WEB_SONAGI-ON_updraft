<template>
    <div>
      <v-card class="group pa-2">
        <v-icon small style="margin-left:5px">home</v-icon>
        <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
      </v-card>
      <v-layout justify-center ma-4>
      <div style="width: 900px;">
        <v-card>
          <v-layout justify-center ma-2>
          <h2>공모전</h2>
          </v-layout>
          <ContestGroup />
        </v-card>
        <v-divider></v-divider>
        <v-card>
          <v-layout justify-center ma-2>
          <h2>행사</h2>
          </v-layout>
          <EventGroup />
        </v-card>
      </div>
      </v-layout>
    </div>
</template>
<script>
import ContestGroup from '../components/ContestGroup'
import EventGroup from '../components/EventGroup'

export default {
  components: { 
    ContestGroup,
    EventGroup,
    },
    data: ()=> ({
      bcLink: [
           {
             text: '대시보드',
             disabled: false,
             href: '/',
           },
           {
             text: '공모전/행사',
             disabled: false,
             href: 'event',
           },
         ],
      
    }),
}
</script>
<style>
    
</style>