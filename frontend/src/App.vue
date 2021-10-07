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
        <v-row no-gutters>
          <v-col>
          <v-expansion-panels accordion>
            <v-expansion-panel outlined>
                <v-list-item link to="/">
                <v-list-item-icon>
                <v-icon>mdi-view-dashboard</v-icon>
                </v-list-item-icon>
                <v-list-item-title>대시보드</v-list-item-title>
            </v-list-item>            </v-expansion-panel>

            <v-expansion-panel outlined>
              <v-expansion-panel-header>
                <v-layout align-center justify-start row fill-height>
                <v-icon class="pa-3">mdi-notebook</v-icon>
                <div>일기</div>
                </v-layout>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-list>
                <v-list-item link to="diary">
                    <v-list-item-title>한눈에 보기</v-list-item-title>
                </v-list-item>
                <v-list-item link to="diary-write">
                    <v-list-item-title>일기 쓰기</v-list-item-title>
                </v-list-item>
                <v-list-item link to="diary-manage">
                    <v-list-item-title>일기 관리</v-list-item-title>
                </v-list-item>
                </v-list>
              </v-expansion-panel-content>
            </v-expansion-panel>
            
            <v-expansion-panel outlined>
              <v-expansion-panel-header>
                <v-layout align-center justify-start row fill-height>
                <v-icon class="pa-3">mdi-view-dashboard</v-icon>
                <div>대시보드</div>
                </v-layout>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                test
              </v-expansion-panel-content>
            </v-expansion-panel>
            
          </v-expansion-panels>
          </v-col>
        </v-row>



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
