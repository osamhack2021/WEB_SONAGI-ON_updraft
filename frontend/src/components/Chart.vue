<template>
  <v-sparkline
    :value="value"
    :gradient="color"
    :smooth="radius || false"
    :padding="padding"
    :line-width="width"
    :stroke-linecap="lineCap"
    :gradient-direction="gradientDirection"
    :fill="fill"
    :type="type"
    :auto-line-width="autoLineWidth"
    auto-draw
    :labels="month"
    color="black" style="max-height: 280px;">
  </v-sparkline>
</template>

<script>
  const color = [
    '#'+((Math.random()*0xFFFFFF<<0)%0xFFFFFF).toString(16),
    '#'+((Math.random()*0xFFFFFF<<0)%0xFFFFFF).toString(16),
    '#'+((Math.random()*0xFFFFFF<<0)%0xFFFFFF).toString(16),
    '#'+((Math.random()*0xFFFFFF<<0)%0xFFFFFF).toString(16)
    ]
    
  export default {
    name: 'Chart',
          
    data: () => ({
      width: 2,
      radius: 10,
      padding: 8,
      lineCap: 'round',      
      gradient: color,
      value: [0,0,8,2,4,2, 5, 9, 0, 10, 3, 5, 1, 8, 2, 0,0,0,0],
      gradientDirection: 'top',
      color,
      fill: false,
      type: 'trend',
      autoLineWidth: true,
      month: ["8월", "9월", "10월", "11월", "12월", "1월","2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월", "1월","2월"]
    }),
    
  }
</script>
