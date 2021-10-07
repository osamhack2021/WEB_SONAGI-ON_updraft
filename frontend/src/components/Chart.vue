<template>
    <v-container fluid>
    <v-sparkline
      :fill="fill"
      :gradient="selectedGradient"
      :line-width="width"
      :padding="padding"
      :smooth="radius || false"
      :value="value"
      auto-draw
    ></v-sparkline>
    </v-container>
</template>

<script>
  export default {
    name: 'Chart',

    data: () => ({
    }),
  }
</script>