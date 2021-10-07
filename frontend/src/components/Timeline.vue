<template lang="">
  <v-card
    class="mx-auto"
    max-width="600"
  >
    <v-card-title
      class="blue-grey white--text"
    >
      <span class="text-h6">Logs</span>
      <v-spacer></v-spacer>
      <v-btn
        :outlined="interval == null"
        :color="interval == null ? 'white' : 'primary'"
        dark
        depressed
        @click="interval == null ? start() : stop()"
      >
        Realtime Logging
      </v-btn>
    </v-card-title>
    <v-card-text class="py-0">
      <v-timeline dense>
        <v-slide-x-reverse-transition
          group
          hide-on-leave
        >
          <v-timeline-item
            v-for="item in items"
            :key="item.id"
            :color="item.color"
            small
            fill-dot
          >
            <v-alert
              :value="true"
              :color="item.color"
              :icon="item.icon"
              class="white--text"
            >
              Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.
            </v-alert>
          </v-timeline-item>
        </v-slide-x-reverse-transition>
      </v-timeline>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: 'Timeline',

    data: () => ({
    }),
  }
</script>

<style lang="">
    
</style>