<template>
    <v-card>
    <v-toolbar>
    <v-toolbar-title>D-{{Math.floor(rcData.remainDays)}}</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-title>전역일 계산기</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-title id="title">입대일: {{userInfo.days[0]}}<br/>전역일: {{userInfo.days[4]}}</v-toolbar-title>
    </v-toolbar>
    
  <v-divider></v-divider>
    <v-container fluid>
        <div>
            <v-row>
                <v-col lg="3" md="3" sm="6" xs="12" class="pb-2">
                    <v-card>
                        <v-row class="no-gutters">
                            <div class="col-auto">
                                <div class="cyan fill-height">&nbsp;</div>
                            </div>
                            <div class="col pa-3 py-4 cyan--text">
                                <h5 class="text-truncate text-uppercase">현재 복무일</h5>
                                <h1><animated-number
                                    :value="rcData.currentDays"
                                    :formatValue="formatToDpDay"
                                    :duration="300"
                                    :round="1"
                                /></h1>
                                <b>{{rcData.discharge_P}}%</b>
                                <v-progress-linear 
                                :rotate="-90"
                                :size="100" 
                                :width="7" 
                                :value="rcData.discharge_P" 
                                color="cyan">

                                </v-progress-linear>
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
                <v-spacer></v-spacer>
                <v-col lg="3" md="3" sm="6" xs="12" class="pb-2">
                    <v-card>
                        <v-row class="no-gutters">
                            <div class="col-auto">
                                <div class="primary fill-height">&nbsp;</div>
                            </div>
                            <div class="col pa-3 py-4 primary--text">
                                <h5 class="text-truncate text-uppercase">남은 복무일</h5>
                                <h1><animated-number
                                    :value="rcData.remainDays"
                                    :formatValue="formatToDmDay"
                                    :duration="300"
                                    :round="1"
                                /></h1>
                                <b>{{rcData.remain_P}}%</b>
                                <v-progress-linear 
                                :rotate="-90"
                                :size="100" 
                                :width="7" 
                                :value="rcData.remain_P" 
                                color="primary">
                                </v-progress-linear>
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
                <v-spacer></v-spacer>
                <v-col lg="3" md="3" sm="6" xs="12" class="pb-2">
                    <v-card>
                        <v-row class="no-gutters">
                            <div class="col-auto">
                                <div class="success fill-height">&nbsp;</div>
                            </div>
                            <div class="col pa-3 py-4 success--text">
                                <h5 class="text-truncate text-uppercase">{{userInfo.classes[rcData.rankIdx+1]}} 진급</h5>
                                <h1><animated-number
                                    :value="rcData.promotion"
                                    :formatValue="formatToDmDay"
                                    :duration="300"
                                    :round="1"
                                /></h1>
                                <b>{{rcData.promotion_P}}%</b>
                                <v-progress-linear :rotate="-90" :size="100" :width="7" :value="rcData.promotion_P" color="success"></v-progress-linear>
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
                <v-spacer></v-spacer>
                <v-col v-show="(!rcData.nmHouse && userInfo.type=='병사')" lg="3" md="3" sm="6" xs="12" class="pb-2">
                    <v-card>
                        <v-row class="no-gutters">
                            <div class="col-auto">
                                <div class="red fill-height">&nbsp;</div>
                            </div>
                            <div class="col pa-3 py-4 red--text">
                                <h5 class="text-truncate text-uppercase" >{{userInfo.classes[rcData.nmRankIdx]}} {{rcData.nmStepIdx}}호봉 진급</h5>
                                <h1><animated-number
                                    :value="rcData.step"
                                    :formatValue="formatToDmDay"
                                    :duration="300"
                                    :round="1"
                                /></h1>
                                <b>{{rcData.step_P}}%</b>
                                <v-progress-linear :rotate="-90" :size="100" :width="7" :value="rcData.step_P" color="red"></v-progress-linear>
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
            </v-row>
        </div>
    </v-container>
    </v-card>
</template>

<style>
    #title {
        font-size: 0.75rem;
    }
    table th + th { border-left:1px solid #dddddd; }
    table td + td { border-left:1px solid #dddddd; }
</style>
<script>
  export default {
    name: 'RetireCalculator',

    data: () => ({
    }),
  }
</script>

<script>
import AnimatedNumber from "animated-number-vue";
import {mapState,mapMutations,mapActions} from 'vuex'

export default {
  components: {
    AnimatedNumber
  },
  computed :{
    ...mapState([
      'rcData',
      "userInfo"
    ]),
  },
  data() {
    return {

    };
  },
  methods: {
    formatToDmDay(value) {
      return `D-${value}`;
    },
    formatToDpDay(value) {
      return `D+${value}`;
    },
    letitbe(){
     this.$store.commit('updateRcData',{
          days : ["2020-08-24","2020-11-01","2021-05-01","2021-11-01","2022-02-23"],       
          classes : ["이등병","일병","상병","병장","민간인"],
          type : "병사"
        }); 
      },
    },
    mounted() {
      setInterval(this.letitbe,300);
    },
};
</script>