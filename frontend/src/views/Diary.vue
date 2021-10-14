<template>
  <div>
    <v-card class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </v-card>
    <Timeline />
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
    }),

    components: {
      Timeline,
    },
  }
</script>

<style>

</style>