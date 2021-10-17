<template>
  <div>
    <v-card class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </v-card>
    <div>
    <RetireCalculator />
    </div>
    <v-divider></v-divider>
    <v-row class="pa-4">
      <v-row align-center>
        <v-flex lg9>
          <v-card class="ma-5 pa-3" style="">
            <div>
              일기 쓴 횟수
            </div>
            <DiaryChart />
          </v-card>
        </v-flex>
        <v-flex lg3>
          <v-card class="col-3 ma-4" style="max-width:300px">
            <DashboardDatePicker />
          </v-card>
        </v-flex>
      </v-row>
    </v-row>
    <v-divider></v-divider>
  </div>
</template>

<script>
  import RetireCalculator from '../components/RetireCalculator'
  import DiaryChart from '../components/DiaryChart'
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
      DiaryChart,
      DashboardDatePicker,
    },
  }
</script>

<style>

</style>