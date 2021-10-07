<template>
    <v-container fluid>
        <div>
            <v-row>
                <v-col lg="3" cols="sm" class="pb-2">
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
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
                <v-col lg="3" cols="sm" class="pb-2">
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
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
                <v-col lg="3" cols="sm" class="pb-2">
                    <v-card>
                        <v-row class="no-gutters">
                            <div class="col-auto">
                                <div class="success fill-height">&nbsp;</div>
                            </div>
                            <div class="col pa-3 py-4 success--text">
                                <h5 class="text-truncate text-uppercase">병장 진급</h5>
                                <h1><animated-number
                                    :value="promotion"
                                    :formatValue="formatToDmDay"
                                    :duration="300"
                                    :round="1"
                                /></h1>
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
                <v-col lg="3" cols="sm" class="pb-2">
                    <v-card>
                        <v-row class="no-gutters">
                            <div class="col-auto">
                                <div class="red fill-height">&nbsp;</div>
                            </div>
                            <div class="col pa-3 py-4 red--text">
                                <h5 class="text-truncate text-uppercase">병장 1호봉 진급</h5>
                                <h1><animated-number
                                    :value="month"
                                    :formatValue="formatToDmDay"
                                    :duration="300"
                                    :round="1"
                                /></h1>
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
            </v-row>
        </div>
    </v-container>
</template>

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
      currentDays: 407,
      remainDays: 142,
      promotion: 28,
      month: 28,
    };
  },
  methods: {
    formatToDmDay(value) {
      return `D-${value}`;
    },
    formatToDpDay(value) {
      return `D+${value}`;
    }
  }
};
</script>