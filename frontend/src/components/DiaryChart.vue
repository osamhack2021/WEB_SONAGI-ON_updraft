<template>
  <div>
    <v-skeleton-loader
      v-if="!isLogin"
      type="image"
    > </v-skeleton-loader>
    <LineChart
      :height="150"
      v-else-if="isLoaded"
      :chartdata="chartdata"
      :options="options">
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
    chartdata: {"labels":[], "datasets": [{"label":"","borderColor": '#FC2525', "data":[]}]},    
    options: {
      legend: {
          display: false
      },
      scales: {
        yAxes: [{
          ticks: {
            min: 0,
            max: 30
          }
        }],
      },
    }
  }),
  computed: {
    ...mapState(['isLogin', 'userdata', 'access_token']),
  },
  methods: {
    updateChart: function(){
      this.chartdata.labels = [];
      let value = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
      let enlisted_date = new Date(this.userdata.enlisted_date);
      let delisted_date = new Date(this.userdata.delisted_date);
      enlisted_date.setDate(1);
      delisted_date.setDate(1);
      while(enlisted_date <= delisted_date){
        this.chartdata.labels.push(enlisted_date.getFullYear()+"-"+(enlisted_date.getMonth()+1));
        enlisted_date.setMonth(enlisted_date.getMonth() + 1);
      }
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
            tmp = tmp.getFullYear()+"-"+(tmp.getMonth()+1);
            let idx = this.chartdata.labels.findIndex((val) => val.includes(tmp));
            value[idx] += 1;
          }
          for(let i = 0; i < this.chartdata.labels.length; i++){
            this.chartdata.labels[i] = this.chartdata.labels[i].split('-')[1]+"월";
          }
          this.chartdata.labels[0] = "입대";
          this.chartdata.labels[this.chartdata.labels.length-1] = "전역";
          this.chartdata.datasets[0].data= value;
          this.isLoaded = true;
        })
    }
  },
  created() {
    if(this.isLogin){
      this.updateChart();
    }
  },
  watch: {
    userdata: function() {
      if(this.isLogin){
        this.updateChart();
      }
    },
    access_token: function() {
      if(this.isLogin){
        this.updateChart();
      }
    }
  },
}
</script>
