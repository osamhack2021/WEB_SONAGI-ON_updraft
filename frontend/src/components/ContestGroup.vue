<template>
        <v-sheet
          class="mx-auto"
        >
          <v-slide-group
            v-model="model"
            class="pa-4"
            center-active
            show-arrows
          >
            <v-slide-item
              v-for="item in contest"
              :key="item"
              v-slot="{ active, toggle }"
            >
              <v-card
                :color="active ? 'primary' : 'grey lighten-1'"
                class="ma-4"
                height="80"
                width="220"
                @click="toggle"
              >
                <v-img
                  height="80"
                  :src=item.img
                ></v-img>
                <v-row
                  class="fill-height"
                  align="center"
                  justify="center"
                >
                </v-row>
              </v-card>
            </v-slide-item>
          </v-slide-group>
          <v-expand-transition>
              <v-sheet
                v-if="model != null"
                height="300"
                tile
              >
                <v-row
                  align="center"
                  justify="center"
                  class="pa-4 ma-4"
                >
                        <h3 class="text-h6" >
                            {{ contest[model].title }}
                        </h3>
                </v-row>
                <v-row
                  align="center"
                  justify="center"
                  class="ma-4"
                >
                    <v-simple-table>
                    <template v-slot:default>
                      <tbody>
                        <tr>
                          <td width="70">주최</td>
                          <td width="500">{{ contest[model].host }}</td>
                        </tr>
                        <tr>
                          <td>일정</td>
                          <td>{{ contest[model].time }}</td>
                        </tr>
                        <tr>
                          <td>분야</td>
                          <td>{{ contest[model].field }}</td>
                        </tr>
                        <tr>
                          <td>링크</td>
                          <td>{{ contest[model].link }}</td>
                        </tr>
                      </tbody>
                    </template>
                  </v-simple-table>
                </v-row>
              </v-sheet>
            </v-expand-transition>
          
        </v-sheet>
</template>

<script>
  export default {
    data: () => ({
      model: null,
      contest:[
        {
          title: "제8회 안전한 학교 공모전 UCC 부문 대국민 심사",
          field: "디자인,UCC/영상,예체능,경품/이벤트",
          time: "2021.10.16 ~ 2021.10.19",
          host: "교육부, 시도교육청",
          link: "https://www.thinkcontest.com/Contest/ContestDetail.html?id=37770",
          img: "https://www.thinkcontest.com/ufiles/contest/59b7e08f4ad92b95a41120c00503e1ddf6ec2755.png",
        },
        {
          title: "(워크숍) 2021 차세대 해외 한국미술 큐레이터 워크숍 참가자 모집",
          field: "예체능/대외활동",
          time: "2021.10.12 ~ 2021.10.25",
          host: "한국국제교류재단",
          link: "https://www.thinkcontest.com/Contest/ContestDetail.html?id=37762",
          img: "https://www.thinkcontest.com/ufiles/contest/8f35bd582956c7f1c9f6236c923381b9047c7dd8.jpg",
        },
        {
          title: "2021년 노동존중 공모전",
          field: "네이밍/슬로건,문학/수기",
          time: "2021.10.13 ~ 2021.10.29",
          host: "노동존중허브센터",
          link: "https://www.thinkcontest.com/Contest/ContestDetail.html?id=37744",
          img: "https://www.thinkcontest.com/ufiles/contest/d39348c54ed82b2d46785420ed3871ba34f5c5e2.png",
        },
        {
          title: "금천구와 함께하는 현직자 직무부트 캠프",
          field: "광고/마케팅,과학/공학,대외활동",
          time: "2021.10.01 ~ 2021.10.23",
          host: "금천구청",
          link: "https://www.thinkcontest.com/Contest/ContestDetail.html?id=37788",
          img: "https://www.thinkcontest.com/ufiles/contest/de24a93e3ed37bba76771b25e60c493ef1b1f144.png",
        },
        {
          title: "SID 잠실종합운동장 영상 공모전",
          field: "UCC/영상",
          time: "2021.10.15 ~ 2021.11.19",
          host: "서울특별시 균형발전본부 동남권사업과",
          link: "https://www.thinkcontest.com/Contest/ContestDetail.html?id=37682",
          img: "https://www.thinkcontest.com/ufiles/contest/3dc98f8200e90855c77d0f6b2e327044cfcfc53d.png",
        },
        {
          title: "2021년 국가연구시설장비 정책․제도 아이디어 및 ZEUS 홍보 콘텐츠 공모전",
          field: "기획/아이디어,디자인,광고/마케팅,UCC/영상",
          time: "2021.10.13 ~ 2021.11.09",
          host: "과학기술정보통신부",
          link: "https://www.thinkcontest.com/Contest/ContestDetail.html?id=37677",
          img: "https://www.thinkcontest.com/ufiles/contest/a2a0c77d0ab70d9255975d7d5884d9094bf6295f.jpg",
        },
        {
          title: "2021 연구실 안전 교육 콘텐츠 공모전 (접수기간 연장, ~ 10/22)",
          field: "기획/아이디어,디자인,UCC/영상,예체능,캐릭터/만화",
          time: "2021.09.16 ~ 2021.10.22",
          host: "과학기술정보통신부, 국가연구안전관리본부",
          link: "https://www.thinkcontest.com/Contest/ContestDetail.html?id=36617",
          img: "https://www.thinkcontest.com/ufiles/contest/d9f93c3c06cad9e24399db58a3faae64800ccdb2.jpg",
        },
        {
          title: "내 손으로 만드는 공연예술창작산실 뉴 슬로건 공모전",
          field: "네이밍/슬로건",
          time: "2021.10.13 ~ 2021.10.27",
          host: "한국문화예술위원회",
          link: "https://www.thinkcontest.com/Contest/ContestDetail.html?id=37645",
          img: "https://www.thinkcontest.com/ufiles/contest/adfa26dccdbc20122440b564b0c945d5b1c550a8.png",
        },
      ],
    }),
  }
</script>