<template>
   <v-app>
      <v-content>
         <v-container fluid fill-height>
            <v-layout align-top justify-center>
               <v-flex xs12 sm8 md4 class="text-center">
                  <v-card class="elevation-12">
                     <v-card-text>
                        로그인이 필요합니다.
                     </v-card-text>
                     <v-card-actions class="justify-center">
                        <v-btn to="/login" elevation="2" color="primary">
                           로그인
                        </v-btn>
                        <v-btn elevation="2" color="primary">
                           회원가입
                        </v-btn>
                     </v-card-actions>
                  </v-card>
               </v-flex>
            </v-layout>
         </v-container>
      </v-content>
   </v-app>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'MainBody',

  data: () => ({
  }),
});
</script>
