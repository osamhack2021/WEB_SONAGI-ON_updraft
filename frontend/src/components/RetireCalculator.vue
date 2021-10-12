<template>
    <v-card>
    <v-toolbar>
    <v-toolbar-title>D-{{Math.floor(remainDays)}}</v-toolbar-title>
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
                                    :value="currentDays"
                                    :formatValue="formatToDpDay"
                                    :duration="300"
                                    :round="1"
                                /></h1>
                                <b>{{discharge_P}}%</b>
                                <v-progress-linear 
                                :rotate="-90"
                                :size="100" 
                                :width="7" 
                                :value="discharge_P" 
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
                                    :value="remainDays"
                                    :formatValue="formatToDmDay"
                                    :duration="300"
                                    :round="1"
                                /></h1>
                                <b>{{remain_P}}%</b>
                                <v-progress-linear 
                                :rotate="-90"
                                :size="100" 
                                :width="7" 
                                :value="remain_P" 
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
                                <h5 class="text-truncate text-uppercase">{{userInfo.classes[rankIdx+1]}} 진급</h5>
                                <h1><animated-number
                                    :value="promotion"
                                    :formatValue="formatToDmDay"
                                    :duration="300"
                                    :round="1"
                                /></h1>
                                <b>{{promotion_P}}%</b>
                                <v-progress-linear :rotate="-90" :size="100" :width="7" :value="promotion_P" color="success"></v-progress-linear>
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
                <v-spacer></v-spacer>
                <v-col v-show="(!nmHouse && userInfo.type=='병사')" lg="3" md="3" sm="6" xs="12" class="pb-2">
                    <v-card>
                        <v-row class="no-gutters">
                            <div class="col-auto">
                                <div class="red fill-height">&nbsp;</div>
                            </div>
                            <div class="col pa-3 py-4 red--text">
                                <h5 class="text-truncate text-uppercase" >{{userInfo.classes[nmRankIdx]}} {{nmStepIdx}}호봉 진급</h5>
                                <h1><animated-number
                                    :value="step"
                                    :formatValue="formatToDmDay"
                                    :duration="300"
                                    :round="1"
                                /></h1>
                                <b>{{step_P}}%</b>
                                <v-progress-linear :rotate="-90" :size="100" :width="7" :value="step_P" color="red"></v-progress-linear>
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

export default {
  components: {
    AnimatedNumber
  },
  data() {
    return {
        userInfo : {},
        tmp : [],
        discharge_P : 0, //전역일 퍼센트
        remain_P : 0, // 남은 복무일 퍼센트
        promotion_P : 0, // 다음 계급 진급일 퍼센트
        step_P : 0,     // 다음 호봉 진급일 퍼센트
        currentDays : 0, // 현재 복무일
        remainDays : 0,  // 남은 복무일
        promotion : 0,   // 다음 계급 진급일
        step : 0,       // 다음 호봉 진급일
        serviceDays : 0, // 전체 복무일
        rankIdx : 0,      // 사용자의 현재 계급idx
        nmRankIdx :0,      //사용자의 현재 계급idx
        stepIdx : 0,      // 사용자의 현재 호봉
        nmStepIdx : 0,     // 사용자음 다음 호봉
        nmHouse : false,   // 다음 달에 전역일 경우
    };
  },
  methods: {
    dateDiff(a,b){
      return (a.getTime()-b.getTime())/(1000*3600*24);
    },
    formatToDmDay(value) {
      return `D-${value}`;
    },
    formatToDpDay(value) {
      return `D+${value}`;
    },
    updateRcData(){
        var ui = {
            days : ["2020-08-24","2020-11-01","2021-05-01","2021-11-01","2022-02-23"],       
            classes : ["이등병","일병","상병","병장","민간인"],
            type : "병사",
        }; this.userInfo = ui;
        var tmp = []; //진급일 배열을 임시로 저장할 배열
        console.log(tmp);
        var idx = 0;  // 사용자의 현재 계급의 인덱스
        var today = new Date(); 
        ui.days.forEach((item)=> {         //tmp를 date객체를 가진 배열로 만들어 준다.
            var list = item.split("-");
            tmp.push(new Date(list[0],list[1]-1,list[2]));
        });
        var all = Math.floor(this.dateDiff(tmp[4],tmp[0]));//총 복무일
        this.serviceDays = all;       
        var cur = Math.floor(this.dateDiff(today,tmp[0])); //현재 복무일
        this.currentDays = cur;
        this.discharge_P = Math.round((this.dateDiff(today,tmp[0]) / all *100)*1000000)/1000000; //전역일 퍼센트
        this.remain_P = Math.round((100-this.discharge_P)*1000000)/1000000.0;
        /*----------------------------------------------------------------------------------------*/
        this.remainDays = (all - cur);                     //남은 복무일
        for(var i=0;i<4;i++){ //현재 계급 구하기
            if(tmp[i].getTime()<=today.getTime() && tmp[i+1].getTime()>today.getTime()){
            idx = i;
            break;
            }
        }
        this.rankIdx = idx;
        var prom = this.dateDiff(tmp[idx+1],today)+1; //다음 계급 진급일
        this.promotion = prom;
        var prodiff = this.dateDiff(tmp[idx+1],tmp[idx]) // 현재 계급 진급일과 다음 계급 진급일 일수 차 구하기
        this.promotion_P = Math.round(((prodiff-prom)/prodiff *100)*1000000)/1000000; // 다음계급 진급일 퍼센트
            /*----------------------------------------------------------------------------------------*/
        var curStep = today.getMonth() - tmp[idx].getMonth() +1;  // 현재 호봉 수
        this.stepIdx = curStep;
        if(today.getMonth()+1 == tmp[idx+1].getMonth()){ //다음달이 진급일이라 호봉 수가 1로 바뀔 때
            if(idx == 3){
            this.nmStepIdx = curStep+1;
            this.nmRankIdx = this.rankIdx;
            }else{
            this.nmStepIdx = 1;
            this.nmRankIdx = this.rankIdx +1;
            }
        } else {        
            this.nmStepIdx = curStep+1;
            this.nmRankIdx = this.rankIdx;
        }
        var tm = new Date(today.getFullYear(),today.getMonth(),1);    //현재 달의 첫날
        var nm = new Date(today.getFullYear(),today.getMonth()+1,1);  //다음 달의 첫날
        var diff = this.dateDiff(nm,tm)       //한달 크기 구하기
        this.step =  this.dateDiff(nm,today)+1;            //다음 호봉 진급일
        if((nm.getTime()-tmp[4].getTime()) > 0 ){                      //다음 달 첫날이 전역 이후 일 때
            this.nmHouse= true;
        }else {
            this.nmHouse = false;
        }
        this.step_P = Math.round(((diff-this.step)/diff *100)*1000000)/1000000; // 다음 호봉 진급일 퍼센트
        
        }
    },
    mounted() {
      this.updateRcData();
    },
};
</script>