<template>
  <div>
      <v-card class="group pa-2">
        <v-icon small style="margin-left:5px">home</v-icon>
        <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
      </v-card>
  <v-layout justify-center ma-2>
  <div>
    <v-card class="pa-2 elevation-0">
    <RetireCalculator />
    </v-card>
    <v-divider></v-divider>
    <v-row class="pa-4" style="width: 1100px;">
      <v-row align-center>
        <v-flex shrink>
          <v-card class="ma-4 pa-3" style="width: 700px; max-width:700px; height: 330px;">
            <div class="pa-2 mb-2">
              일기 쓴 횟수
            </div>
            <DiaryChart />
          </v-card>
        </v-flex>
        <v-flex shrink>
          <v-card class="col-3 pa-3 ma-4" style="min-width:310px; height:330px;">
            <DashboardDatePicker />
          </v-card>
        </v-flex>
      </v-row>
    </v-row>
    <v-divider></v-divider>
    <v-row>
      <v-col style="width: 500px">
        <EventGroup />
      </v-col>
      <v-col style="width: 500px">
        <ContestGroup />
      </v-col>
    </v-row>
  </div>
  </v-layout>
  </div>
</template>

<script>
  import RetireCalculator from '../components/RetireCalculator'
  import DiaryChart from '../components/DiaryChart'
  import DashboardDatePicker from '../components/DashboardDatePicker'
  import EventGroup from '../components/EventGroup'
  import ContestGroup from '../components/ContestGroup'

  export default {
    name: 'Home',

    data: ()=> ({
      bcLink: [
           {
             text: '대시보드',
             disabled: false,
             href: '/',
           },
         ],
    }),

    components: {
      RetireCalculator,
      DiaryChart,
      DashboardDatePicker,
      EventGroup,
      ContestGroup,
    },
  }
</script>

<style>

</style>