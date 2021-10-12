<template>
<v-layout align-center justify-center row fill-height class="py-8 px-4">
  <v-card class="py-8 px-4 ma-4" style="max-width: 900px;">
      <div class="scroll-box">  
        <v-timeline dense v-for="(v,k) in diaryData" :key="k">
          <v-timeline-item v-for="item in v" :key="item" :icon="item.emotion" :color="'#'+((Math.random()*0xFFFFFF<<0)%0xFFFFFF).toString(16)">
            <v-card class="pa-2 ma-2">
              <v-layout align-center justify-space-between row fill-height class="pa-2 ma-2">
              <v-card-title>{{item.title}}</v-card-title>
              <v-btn depressed color="white" link to="/diary-write">
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
              
              </v-layout>
              <v-card class="pa-2 ma-2" :elevation="0">
              {{item.content}}
              </v-card>
              
              <div class="text-right">{{item.published_at}}</div>
            </v-card>
          </v-timeline-item>
        </v-timeline>
      </div>
  </v-card>
</v-layout>
</template>

<script>
  export default {
    name: 'Timeline',

    data: () => ({
      diaryData: {
      'August, 2020': [
        {
          title: '입대',
          content: 'holy-shit',
          emotion: 'mdi-emoticon-dead-outline',
          published_at: '2020-08-24'
        },
      ],
      'November, 2020': [
        {
          title: '일병 진급',
          content: '좋긴 한데.... 아직 한참남았네? 이제 시작인가?',
          emotion: 'mdi-emoticon-excited-outline',
          published_at: '2020-11-01'
        },
        {
          title: '생일',
          content: '군대에서 생일이라니. 카톡으로 선물은 많이 받았지만 군대라서 기분은 썩 좋지 않다. 선물이 무슨 의미야! 쓰지도 못하는데! 퓨..',
          emotion: 'mdi-emoticon-angry-outline',
          published_at: '2020-11-20'
        },
      ],
      'May, 2021': [
        {
          title: '상병 진급',
          content: '좋긴 한데.... 아직 반도 안했네? 언제 집가지?',
          emotion: 'mdi-emoticon-cool-outline',
          published_at: '2021-05-01'
        },
        {
          title: '청원 휴가를 나갔다',
          content: '결국 스노우볼이 이렇게 흘러 인대 파열로 수술을 하게 됐다. 마음이 좋진 않지만 빨리 회복 하고 다시 돌아올 수 있으면 좋겠다.',
          emotion: 'mdi-emoticon-neutral-outline',
          published_at: '2021-05-04'
        },
      ],
      'October, 2021': [
        {
          title: '군장병 해커톤 화이팅',
          content: '오늘은 해커톤 대회 준비를 하는 중에 이발병에게 카톡이와서 머리를 자르고 왔더니 격리를 하래서 대회 준비를 못했다. 내일 결과가 나올까? 심란하다. 아직 다 준비가 안됐는데 ㅅㅂ ㅈ됐다. 이러다가 대회 마무리 못하면 ㅈㄷㅎ중사님 각오하십쇼',
          emotion: 'mdi-emoticon-confused-outline',
          published_at: '2021-10-11'
        }
      ]
    }
    /*
    title (한줄평)
    content (내용)
    emotion (감정 : 행복, 보통, 별로, 슬픔 등)
      mdi-emoticon-angry-outline
      mdi-emoticon-confused-outline
      mdi-emoticon-cool-outline
      mdi-emoticon-cry-outline
      mdi-emoticon-dead-outline
      mdi-emoticon-excited-outline
      mdi-emoticon-neutral-outline
      mdi-emoticon-sad-outline
      mdi-emoticon-sick-outline
      mdi-star-face
    write_date (작성 일시)
    rewrite_date (마지막 수정 일자) */
    }),
    
  }
</script>

<style lang="">
    
</style>