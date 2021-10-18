<template>
  <div>
    <v-skeleton-loader
        v-if="!isLogin"
        type="image"
      > </v-skeleton-loader>
    <v-date-picker
      v-else
      locale="ko-kr"
      v-model="date2"
      :event-color="date => date[9] % 2 ? 'red' : 'yellow'"
      :events="functionEvents"
      show-adjacent-months
      no-title
    ></v-date-picker>
  </div>
</template>

<script>
import { mapState } from 'vuex';
  export default {
    name: 'Chart',

    data: () => ({
      arrayEvents: null,
      date1: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      date2: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    }),

    mounted () {
      this.arrayEvents = [...Array(6)].map(() => {
        const day = Math.floor(Math.random() * 30)
        const d = new Date()
        d.setDate(day)
        return d.toISOString().substr(0, 10)
      })
    },
    computed: {
        ...mapState(['isLogin', 'userdata']),
      },
    methods: {
      functionEvents (date) {
        const [,, day] = date.split('-')
        if ([12, 17, 28].includes(parseInt(day, 10))) return true
        if ([1, 19, 22].includes(parseInt(day, 10))) return ['red', '#00f']
        return false
      },
    },
  }
</script>