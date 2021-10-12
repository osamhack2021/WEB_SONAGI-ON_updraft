<template lang="">
    <div>
    <span class="group pa-2">
      <v-icon small style="margin-left:5px">home</v-icon>
      <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
    </span>
        
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
             text: '일기',
             disabled: false,
             href: 'diary',
           },
           {
             text: '일기 관리',
             disabled: false,
             href: 'diary-manage',
           },
         ],
    }),
}
</script>
<style lang="">
    
</style>