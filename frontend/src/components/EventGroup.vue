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
                height="420"
                width="300"
                @click="toggle"
              >
                <v-img
                  height="420"
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
                          <td width="90">일정</td>
                          <td width="700">{{ contest[model].time }}</td>
                        </tr>
                        <tr>
                          <td>지역</td>
                          <td>{{ contest[model].field }}</td>
                        </tr>
                        <tr>
                          <td>상세정보</td>
                          <td>{{ contest[model].host }}</td>
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
          title: "[국립무형유산원] K - 무형유산 페스티벌",
          time: "2021.10.16 ~ 2021.10.19",
          field: "서울",
          host: "국립무형유산원 중정 및 야외 공연장",
          link: "https://www.culture.go.kr/festival/festivalView.do?uci=G7061633485148406&seq=171246&cPage=1",
          img: "https://www.culture.go.kr/upload/rdf/21/10/rdf_2021100610522801762.jpg",
        },
        {
          title: "코카카 로고송 공모전 안내벌",
          time: "2021-09-06~2021-10-17",
          field: "서울",
          host: "코카카 로고송 공모전",
          link: "https://www.culture.go.kr/festival/festivalView.do?uci=G7061631798054872&seq=170637&cPage=1",
          img: "https://www.culture.go.kr/upload/rdf/21/09/show_2021091613141478097.jpg",
        },
        {
          title: "2021 관악강감찬축제",
          time: "2021-10-01~2021-10-17",
          field: "서울",
          host: "낙성대공원, 별빛내린천 /온라인 공간",
          link: "https://www.culture.go.kr/festival/festivalView.do?uci=G7061633428965219&seq=171190&cPage=1",
          img: "https://www.culture.go.kr/upload/rdf/21/10/rdf_202110051916546618.jpg",
        },
        {
          title: "2021 전주문화재야행",
          time: "2021-10-22~2021-10-22",
          field: "전북",
          host: "2021 전주문화재야행",
          link: "https://www.culture.go.kr/festival/festivalView.do?uci=G7061631687234488&seq=170580&cPage=1",
          img: "https://www.culture.go.kr/upload/rdf/21/09/rdf_2021091515271440823.jpg",
        },
        {
          title: "[세계유산 미디어아트] 2021 수원화성 미디어아트쇼",
          time: "2021.10.16 ~ 2021.10.19",
          field: "경기",
          host: "수원화성 화서문 , 서북공심돈 일원",
          link: "https://www.culture.go.kr/festival/festivalView.do?uci=G7061633506662389&seq=171249&cPage=1",
          img: "https://www.culture.go.kr/upload/rdf/21/10/rdf_202110061651248072.JPG",
        },
      ],
    }),
  }
</script>