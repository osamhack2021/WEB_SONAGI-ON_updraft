<template>
   <v-card
      class="mx-auto"
      width="300"
      >
      <v-list>
         <v-list-item link to="/">
            <v-list-item-icon>
               <v-icon>mdi-view-dashboard</v-icon>
            </v-list-item-icon>
            <v-list-item-title>대시보드</v-list-item-title>
         </v-list-item>
         <v-list-group
            :value="false"
            prepend-icon="mdi-notebook"
            >
            <template v-slot:activator>
               <v-list-item-title>일기</v-list-item-title>
            </template>
            <v-list class="px-4">
               <v-list-item link to="/diary">
                  <v-list-item-icon>
                     <v-icon>mdi-eye</v-icon>
                  </v-list-item-icon>
                  <v-list-item-title>한눈에 보기</v-list-item-title>
               </v-list-item>
               <v-list-item link to="/diary-write">
                  <v-list-item-icon>
                     <v-icon>mdi-book-edit</v-icon>
                  </v-list-item-icon>
                  <v-list-item-title>일기 쓰기</v-list-item-title>
               </v-list-item>
               <v-list-item link to="/diary-manage">
                  <v-list-item-icon>
                     <v-icon>mdi-book-cog</v-icon>
                  </v-list-item-icon>
                  <v-list-item-title>일기 관리</v-list-item-title>
               </v-list-item>
            </v-list>
         </v-list-group>
         <v-list-item link to="calendar">
            <v-list-item-icon>
               <v-icon>mdi-calendar-month-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>캘린더</v-list-item-title>
         </v-list-item>
         <v-list-item link to="community">
            <v-list-item-icon>
               <v-icon>mdi-account-group</v-icon>
            </v-list-item-icon>
            <v-list-item-title>커뮤니티</v-list-item-title>
         </v-list-item>
         <v-list-item link to="event">
            <v-list-item-icon>
               <v-icon>mdi-bullhorn</v-icon>
            </v-list-item-icon>
            <v-list-item-title>공모전/행사</v-list-item-title>
         </v-list-item>
         <v-list-item link to="self-care">
            <v-list-item-icon>
               <v-icon>mdi-dumbbell</v-icon>
            </v-list-item-icon>
            <v-list-item-title>자기관리</v-list-item-title>
         </v-list-item>
      </v-list>
   </v-card>
</template>


<script>
   export default {
     name: 'Category',
   
     data: () => ({
     }),
   }
</script>