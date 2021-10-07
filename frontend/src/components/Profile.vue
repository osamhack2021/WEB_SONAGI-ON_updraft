<template>
   <v-card height="350px" class="d-flex align-center justify-center">
      <v-list>
         <v-list-item>
            <v-icon size=150>mdi-account-circle</v-icon>
         </v-list-item>
         <v-list-item link>
            <v-list-item-content>
               <v-list-item-title class="text-h5 d-flex align-center justify-center">NAME</v-list-item-title>
               <v-list-item-subtitle class="d-flex align-center justify-center">CLASS</v-list-item-subtitle>
            </v-list-item-content>
         </v-list-item>
      </v-list>
   </v-card>
</template>

<script>
   export default {
     name: 'Profile',
   
     data: () => ({
     }),
   }
</script>