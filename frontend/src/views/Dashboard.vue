<template>
  <div>
    <RetireCalculator />
    <v-divider></v-divider>
    <Chart />
  </div>
</template>

<script>
  import RetireCalculator from '../components/RetireCalculator'
  import Chart from '../components/Chart'

  export default {
    name: 'Home',

    components: {
      RetireCalculator,
      Chart,
    },
  }
</script>

<style>

</style>