<template>
  <v-menu
    v-model="menu"
    :close-on-content-click="false"
    :nudge-right="40"
    transition="scale-transition"
    offset-y
    min-width="auto"
  >
    <template v-slot:activator="{ on, attrs }">
    <v-text-field
      v-model="date"
      v-bind:label="label"
      prepend-icon="mdi-calendar"
      readonly
      v-bind="attrs"
      v-on="on"
    ></v-text-field>
    </template>
    <v-date-picker
      locale="ko-kr"
      v-model="date"
      @input="menu=false"
      :show-current="false"
    ></v-date-picker>
  </v-menu>
</template>

<script>
// https://mine-it-record.tistory.com/364
// $$ 중요 https://juntcom.tistory.com/103
export default {
  props: ['type', 'label', 'propDate'],
  name: "UserSettingDatePicker",
  data: () => ({
    menu: false,
  }),
  computed: { 
    date: { 
      get () { 
        return this.propDate;
      }, 
      set (newDate) { 
        let type = this.type;
        this.$emit('date-extract', {type, newDate});
      } 
    } 
  },
}
</script>
