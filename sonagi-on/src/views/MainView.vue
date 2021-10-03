<template>
  <MainBody />
</template>

<script lang="ts">
import Vue from 'vue';
import MainBody from '../components/MainBody.vue';

export default Vue.extend({
  name: 'MainView',

  components: {
    MainBody,
  },
});
</script>
