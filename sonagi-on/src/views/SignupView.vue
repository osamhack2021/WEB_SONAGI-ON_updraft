<template>
  <SignupForm />
</template>

<script lang="ts">
import Vue from 'vue';
import SignupForm from '../components/SignupForm.vue';

export default Vue.extend({
  name: 'SignupView',

  components: {
    SignupForm,
  },
});
</script>
