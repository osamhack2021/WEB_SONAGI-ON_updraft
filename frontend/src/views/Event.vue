<template>
    <div>
    <v-card class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </v-card>
      <ContestGroup />
      <EventGroup />
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
             href: 'Dashboard',
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