<template>
  <div>
    <div class="py-4">
    <RetireCalculator />
    </div>
    <v-divider></v-divider>
    <v-row class="py-4">
      <v-col class="col-9">
        <Chart />
      </v-col>
      <v-col class="col-3">
        <DashboardDatePicker />
      </v-col>
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

    components: {
      RetireCalculator,
      Chart,
      DashboardDatePicker,
    },
  }
</script>

<style>

</style>