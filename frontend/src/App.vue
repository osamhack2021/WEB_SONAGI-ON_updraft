<template>
   <!-- App.vue -->
   <v-app class="myFont">

      <!-- 좌측 네비게이션 바 -->
      <v-card>
         <v-navigation-drawer app permanent>
            <Profile />
            <Category />
         </v-navigation-drawer>
      </v-card>

      <!-- 상단 바 -->
      <v-app-bar app class="text-h4 bold" height="80px">
         <v-row>
            <v-col class="appBarFont ma-5 pl-5">
               <div>{{ $route.name }}</div>
            </v-col>
            <v-col align="right">
               <router-link to="/">
                  <v-avatar height="80px" width="120px" :tile="true">
                     <img :src="require('@/assets/LOGO.png')" alt="logo" link to="/">
                  </v-avatar>
               </router-link>
            </v-col>
         </v-row>
      </v-app-bar>

      <!-- Sizes your content based upon application components -->
      <v-main>
         <span class="group pa-2">
            <v-icon small style="margin-left:5px">home</v-icon>
            <v-breadcrumbs :items="items"></v-breadcrumbs>
         </span>
         <router-view />
         <!-- Provides the application the proper gutter -->
      </v-main>

      <!-- foooooooooooooooooooooooooooooooooooooooooooooooooteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeer-->
      <v-footer
         color="grey lighten-1"
         padless
         >
         <v-row
            justify="center"
            no-gutters
            >
            <v-col
               class="grey lighten-2 py-3 text-center"
               cols="12"
               >
               {{ new Date().getFullYear() }} — <strong>Updraft</strong>
            </v-col>
         </v-row>
      </v-footer>
   </v-app>
</template>

<script>
   import Category from './components/Category.vue';
   import Profile from './components/Profile.vue';
   
   export default {
     name: 'App',
   
     components: {
         Profile,
         Category,
     },
   
 
         data: ( ) => ({/*
       items: [
           {
             text: 'Dashboard',
             disabled: false,
             href: 'Dashboard',
           },
           {
             text: 'Link 1',
             disabled: false,
             href: 'breadcrumbs_link_1',
           },
           {
             text: 'Link 2',
             disabled: true,
             href: 'breadcrumbs_link_2',
           },
         ],*/
     }),
   };
</script>

<style>
   @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');
   @import url('https://fonts.googleapis.com/css2?family=Song+Myung&display=swap');

   .myFont {
      font-family: 'Gowun Dodum', sans-serif;
   }
   .appBarFont {
      font-family: 'Song Myung', serif;
   }
   .group {
   display: flex;
   flex: 1;
   }
</style>