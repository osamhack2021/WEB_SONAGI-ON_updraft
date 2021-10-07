<template>
  <!-- App.vue -->

<v-app>
    <v-card>
    <v-navigation-drawer app permanent>
      <v-card height="350px" class="d-flex align-center justify-center">
        <v-list>
          <v-list-item>
            <v-avatar size=150 >
              <v-img 
                height=150px
                src="https://www.unmc.edu/cihc/_images/faculty/default.jpg"
              ></v-img>
            </v-avatar>
          </v-list-item>

          <v-list-item link>
            <v-list-item-content>
              <v-list-item-title class="text-h5 d-flex align-center justify-center">NAME</v-list-item-title>
              <v-list-item-subtitle class="d-flex align-center justify-center">CLASS</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card>
      
            <v-list
            nav
            dense
            >
            <v-list-item link to="/">
                <v-list-item-icon>
                <v-icon>mdi-view-dashboard</v-icon>
                </v-list-item-icon>
                <v-list-item-title>대시보드</v-list-item-title>
            </v-list-item>
            <v-list-item link to="diary">
                <v-list-item-icon>
                <v-icon>mdi-notebook</v-icon>
                </v-list-item-icon>
                <v-list-item-title>일기</v-list-item-title>
            </v-list-item>

            <v-list-item link to="diary">
                <v-list-item-icon>
                <v-icon>mdi-notebook</v-icon>
                </v-list-item-icon>
                <v-list-item-title>일기</v-list-item-title>
                <v-expansion-panels accordion flat >
                  <v-expansion-panel accordion>
                    <v-expansion-panel-content>
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
            </v-list-item>
            
            

            
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
      <template v-slot:append>
        
      </template>
    </v-navigation-drawer>
    </v-card>

  <v-app-bar app class="text-h4 bold" height="80px">
    <v-row>
      <v-col>
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
        class="grey lighten-2 py-4 text-center"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Updraft</strong>
      </v-col>
    </v-row>
  </v-footer>
</v-app>
    
</template>



<script>

export default {
  name: 'App',

  data: () => ({/*
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
.group {
  display: flex;
  flex: 1;
}
</style>
