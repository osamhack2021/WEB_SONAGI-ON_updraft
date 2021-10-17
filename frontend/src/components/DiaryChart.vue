<template>
  <div>
    <v-skeleton-loader
      v-if="!isLogin"
      type="image"
    > </v-skeleton-loader>
    <LineChart
      v-else-if="isLoaded"
      :chartdata="chartdata"
      :options="{}">
    </LineChart>
  </div>
</template>

<script>
import LineChart from './side_modules/LineChart.vue'
import { mapState } from 'vuex';
  
export default {
  components: { LineChart },
  name: 'DiaryChart',
  data: () => ({
    isLoaded: false,
    chartdata: {},    
    value: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    month: ["입대", "4월", "5월", "6월", "7월", "8월","9월", "10월", "11월", "12월", "1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월","전역"]
  }),
  computed: {
    ...mapState(['isLogin', 'userdata', 'access_token']),
  },
  methods: {
    updateChart: function(){
      let enlisted_date = new Date(this.userdata.enlisted_date);
      let delisted_date = new Date(this.userdata.delisted_date);
      enlisted_date.setDate(1);
      delisted_date.setDate(1);
      this.month = ["입대"];
      while(enlisted_date < delisted_date){
        enlisted_date.setMonth(enlisted_date.getMonth() + 1);
        this.month.push((enlisted_date.getMonth()+1)+"월");
      }
      this.month[this.month.length-1] = "전역";
      const config = {
        headers: {
          Authorization: `Bearer ${this.access_token}`,
        },
      };
      this.axios
        .get(`${this.$store.state.BACKEND_URL}/api/diary/list`, config)
        .then((res) => {
          for(let i = 0; i < res.data.length; i++){
            let tmp = new Date(res.data[i]['write_date']);
            tmp = (tmp.getMonth()+1)+"월";
            console.log(tmp);
            let idx = this.month.findIndex((val) => val.includes(tmp));
            this.value[idx] += 1;
          }
          this.chartdata.labels = this.month;
          this.chartdata.datasets = this.value;
          this.isLoaded = true;
        })
    }
  },
  created() {
    this.updateChart();
  },
  watch: {
    userdata: function() {
      this.updateChart();
    },
  },
}
</script>
