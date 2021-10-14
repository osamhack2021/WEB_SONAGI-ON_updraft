<template>
  <div>
    <span class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </span>
    <div class="py-4">
    <RetireCalculator />
    </div>
    <v-divider></v-divider>
    <v-row class="py-4">
      <v-layout justify-space-around>
      <v-card class="col-9 ma-4">
        <div>
          일기 쓴 횟수
        </div>
        <Chart />
      </v-card>
      <v-card class="col-3 ma-4" style="max-width: 300px;">
        <v-layout justify-center>
        <DashboardDatePicker />
        </v-layout>
      </v-card>
      </v-layout>
    </v-row>
    <v-divider></v-divider>
  </div>
</template>

<script>
  import RetireCalculator from '../components/RetireCalculator'
  import Chart from '../components/Chart'
  import DashboardDatePicker from '../components/DashboardDatePicker'

  export default {
    name: 'Home',

    data: ()=> ({
      bcLink: [
           {
             text: '대시보드',
             disabled: false,
             href: 'Dashboard',
           },
         ],
    }),

    components: {
      RetireCalculator,
      Chart,
      DashboardDatePicker,
    },
  }
</script>

<style>

</style>