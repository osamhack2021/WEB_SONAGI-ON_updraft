<template>
    <div>
    <span class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </span>
        Calendar page
    </div>
</template>
<script>
export default {
    data: ()=> ({
      bcLink: [
           {
             text: '대시보드',
             disabled: false,
             href: 'Dashboard',
           },
           {
             text: '캘린더',
             disabled: false,
             href: 'calendar',
           },
         ],
    }),
    
}
</script>
<style>
    
</style>