<template>
  <v-layout justify-center>
    <v-card style="width: 900px;">
       <v-container fluid>
       <v-toolbar>
            <v-toolbar-title >휴가 관리</v-toolbar-title>
       </v-toolbar>
        <div class="mt-3">
            <v-row>
                <v-spacer></v-spacer>
                <v-col lg="3" md="3" sm="3" xs="12" class="pb-2">
                    <v-card>
                        <v-row class="no-gutters text-center">
                            <div class="col-auto">
                                <div class="cyan fill-height">&nbsp;</div>
                            </div>
                            <div class="col pa-3 py-4 cyan--text">
                                <h4 class="text-truncate text-uppercase">전체 휴가일</h4>
                                <h1>{{all()}}</h1>
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
                <v-spacer></v-spacer>
                <v-col lg="3" md="3" sm="3" xs="12" class="pb-2">
                    <v-card>
                        <v-row class="no-gutters text-center">
                            <div class="col-auto">
                                <div class="red fill-height">&nbsp;</div>
                            </div>
                            <div class="col pa-3 py-4 red--text">
                                <h4 class="text-truncate text-uppercase">사용 휴가일</h4>
                                <h1>{{use()}}</h1>
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
                <v-spacer></v-spacer>
                <v-col lg="3" md="3" sm="3" xs="12" class="pb-2">
                    <v-card>
                        <v-row class="no-gutters text-center">
                            <div class="col-auto">
                                <div class="success fill-height">&nbsp;</div>
                            </div>
                            <div class="col pa-3 py-4 success--text">
                                <h4 class="text-truncate text-uppercase">남은 휴가일</h4>
                                <h1>{{left()}}</h1>
                            </div>
                        </v-row>
                    </v-card>
                </v-col>
                <v-spacer></v-spacer>
            </v-row>
        </div>
        </v-container>
        <v-divider></v-divider>
        <v-container>
            <v-row>
                <v-col><v-btn text @click="filterList(99)">전체</v-btn></v-col>
                <v-col><v-btn text @click="filterList(4)">정기</v-btn></v-col>
                <v-col><v-btn text @click="filterList(1)">보상</v-btn></v-col>
                <v-col><v-btn text @click="filterList(0)">포상</v-btn></v-col>
                <v-col><v-btn text @click="filterList(2)">위로</v-btn></v-col>
                <v-col><v-btn text @click="filterList(3)">청원</v-btn></v-col>
                <v-col><v-btn text @click="filterList(5)">외박</v-btn></v-col>
                <v-col><v-btn text @click="filterList(6)">기타</v-btn></v-col>
            </v-row>
        </v-container>
        <v-divider></v-divider>
        <div style="overflow:auto; height:500px">
        <template>
            <v-list-item  v-for="(vc,i) in filterVmp" :key="i">
                <v-list-item-content>
                    <v-container>
                        <v-row :class="vc.usedS.idx==vc.termS.idx ? 'grey' : 'white'">
                        <v-col>
                            <h2>{{vc.name}}</h2><h4>{{vType[vc.type]}} 휴가/{{vc.day}} 받음</h4>
                        </v-col>
                    <v-spacer></v-spacer>
                        <v-col align="right" align-self="center">
                            <h2>({{vc.usedS.idx}}일/{{vc.termS.idx}}일)</h2>
                        </v-col>
                        <v-col cols="auto" align-self="center">
                            <v-dialog
                            width="500"
                            persistent
                            v-model="vc.dialog"
                            >
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn
                                :color="vc.usedS.idx==vc.termS.idx ? 'white' : 'grey'"
                                dark
                                v-bind="attrs"
                                v-on="on"
                                icon
                                >
                                <v-icon>mdi-cog</v-icon>
                                </v-btn>
                            </template>
                            
                            <v-card>
                                <v-card-title class="text-h5 grey lighten-2">
                                휴가 수정하기
                                </v-card-title>
                                
                                <v-container>
                                    <v-form
                                        ref="form"
                                        lazy-validation
                                    >
                                    <v-row>
                                        <v-col cols="auto" align-self="center">휴가 이름 :</v-col>
                                        <v-col><v-text-field
                                        v-model="vmp[i].name"
                                        :rules="nameRules"    
                                        required                                                                        
                                    ></v-text-field></v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col cols="auto" align-self="center">휴가 타입 :</v-col>
                                        <v-col>
                                        <v-radio-group v-model="vmp[i].type" row>
                                        <v-radio
                                            v-for="(n,idx) in vType"
                                            :key="idx"
                                            :label="`${n} 휴가`"
                                        ></v-radio>
                                        </v-radio-group>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col cols="auto" align-self="center">받은 날짜 :</v-col>
                                        <v-col>
                                        <v-text-field
                                        v-model="vmp[i].day"                         
                                        hint="YYYY-MM-DD"
                                        :rules="vcDay_rule"
                                        persistent-hint
                                        required
                                        ></v-text-field>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col cols="auto" align-self="center">총 일수 :</v-col>
                                        <v-col>
                                        <v-select
                                        v-model="vmp[i].termS"
                                        :items="termList.filter((el,index)=>{
                                            return index > 0
                                        })"
                                        item-text="tag"
                                        item-value="idx"
                                        label="Standard"
                                        return-object
                                        ></v-select>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col cols="auto" align-self="center">사용한 일수 :</v-col>
                                        <v-col>
                                        <v-select
                                        v-model="vmp[i].usedS"
                                        :items="termList.filter((el,index)=>{
                                            return index <= vmp[i].termS.idx
                                        })"
                                        item-text="tag"
                                        item-value="idx"
                                        label="Standard"
                                        return-object
                                        ></v-select>
                                        </v-col>
                                    </v-row>
                                    </v-form> 
                                </v-container>
                                             
                                <v-divider></v-divider>
                                <v-card-actions>
                                <v-dialog
                                v-model="vc.dialogs"
                                width="500"
                                >
                                <template v-slot:activator="{ on, attrs }">
                                    <v-btn
                                    color="red lighten-2"                                 
                                    v-bind="attrs"
                                    v-on="on"
                                    >
                                    삭제하기
                                    </v-btn>
                                </template>

                                <v-card>
                                    <v-card-title>Delete</v-card-title>
                                    <v-card-text>
                                    정말로 삭제하시겠습니까? 삭제하신 휴가 정보는 되돌릴 수 없습니다.
                                    </v-card-text>

                                    <v-divider></v-divider>

                                    <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn
                                        color="primary"
                                        text
                                        @click="vc.dialogs = false; vc.dialog=false; deleteV(i) ;"
                                    >
                                        확인
                                    </v-btn>
                                    </v-card-actions>
                                </v-card>
                                </v-dialog>
                                <v-spacer></v-spacer>
                                <v-btn
                                    color="primary"
                                    text
                                    @click="vc.dialog = false; changeInfo(i)"
                                >
                                    확인
                                </v-btn>
                                <v-btn
                                    color="red"
                                    text
                                    @click="vc.dialog = false; resetDefault()"
                                >
                                    취소
                                </v-btn>
                                </v-card-actions>
                            </v-card>
                            </v-dialog>
                        </v-col>
                        </v-row>              
                    </v-container>    
                </v-list-item-content>
            </v-list-item>
        </template>
        </div>
        <v-divider></v-divider>
        <div>
        <v-dialog
        width="500"
        persistent
        v-model="newV.dialog"
        >
        <template v-slot:activator="{ on, attrs }">
            <div align="center"><v-btn
            color="black"
            dark
            v-bind="attrs"
            v-on="on"
            @click="resetAdd()"
            >
            <v-icon>mdi-plus</v-icon>
            </v-btn></div>
        </template>
        
        <v-card>
            <v-card-title class="text-h5 grey lighten-2">
            휴가 추가하기
            </v-card-title>
            
            <v-container>
                <v-form
                    ref="form"
                    lazy-validation
                    id="add-vacation-form"
                    @submit.prevent="addVacation"
                >
                <v-row>
                    <v-col cols="auto" align-self="center">휴가 이름 :</v-col>
                    <v-col><v-text-field
                    v-model="newV.name"
                    :rules="nameRules"    
                    required                                                                        
                ></v-text-field></v-col>
                </v-row>
                <v-row>
                    <v-col cols="auto" align-self="center">휴가 타입 :</v-col>
                    <v-col>
                    <v-radio-group v-model="newV.type" row>
                    <v-radio
                        v-for="(n,idx) in vType"
                        :key="idx"
                        :label="`${n} 휴가`"
                    ></v-radio>
                    </v-radio-group>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="auto" align-self="center">받은 날짜 :</v-col>
                    <v-col>
                    <v-text-field
                    v-model="newV.day"                         
                    hint="YYYY-MM-DD"
                    :rules="vcDay_rule"
                    persistent-hint
                    required
                    ></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="auto" align-self="center">총 일수 :</v-col>
                    <v-col>
                    <v-select
                    v-model="newV.termS"
                    :items="termList.filter((el,index)=>{
                        return index > 0
                    })"
                    item-text="tag"
                    item-value="idx"
                    label="Standard"
                    return-object
                    ></v-select>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="auto" align-self="center">사용한 일수 :</v-col>
                    <v-col>
                    <v-select
                    v-model="newV.usedS"
                    :items="termList.filter((el,index)=>{
                        return index <= newV.termS.idx
                    })"
                    item-text="tag"
                    item-value="idx"
                    label="Standard"
                    return-object
                    ></v-select>
                    </v-col>
                </v-row>
                </v-form> 
            </v-container>
                            
            <v-divider></v-divider>
            <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                color="primary"
                text
                type="submit"
                form="add-vacation-form"
            >
                확인
            </v-btn>
            <v-btn
                color="red"
                text
                @click="closeD()"
            >
                취소
            </v-btn>
            </v-card-actions>
            
        </v-card>
        </v-dialog>
        </div>
    </v-card>
  </v-layout>
</template>
<script>
import {mapState} from 'vuex'
export default {
  components: {

  },
  data() {
    return {
      nameRules: [
        v => !!v || 'Name is required',
      ],
      vcDay_rule :[
        v => !!v || 'Day is required',
        v=> /^[0-9-]*$/.test(v) || '형식에 맞춰서 입력해주세요'
      ],
      vType : [
        "포상","보상","위로","청원","정기","외박","기타"
      ],
      vmp : [],
      filterVmp:[],
      termList :[],
      newV :{
        name : "",
        type: 0,
        day : "",
        dialog: false,
        dialogs:false,
        termS : {tag:"",idx:0},
        usedS : {tag:"",idx:0}
      },
      node: null,
    }
  },
  methods :{
    resetDefault() {
      this.callVCInfo();
    },
    changeInfo(idx) {      
      const config = {
        headers: {
          Authorization: `Bearer ${this.access_token}`,
        },
      };
      let target = this.filterVmp[idx];
      target = {"id":target.id, "name":target.name, "day":target.day, "type":target.type, "usedS": target.usedS.idx, "termS": target.termS.idx};
      this.axios.post(`${this.$store.state.BACKEND_URL}/api/vacation/rewrite`,target, config)
        .then(()=>{
          this.$alert("성공적으로 수정했습니다.","","success");
          this.resetDefault();
        });
    },
    makeTerm() {
      this.termList.push({tag:"미사용", idx:0})
      for(var i = 1;i<=50;i++){
          this.termList.push({tag:(i-1)+"박 "+i+"일",idx:i});
      }
    },
    deleteV(idx){
      const config = {
        headers: {
          Authorization: `Bearer ${this.access_token}`,
        },
      };
      let id = this.filterVmp[idx].id;
      this.axios.post(`${this.$store.state.BACKEND_URL}/api/vacation/delete`, {id}, config)
        .then(()=>{
          this.$alert("성공적으로 삭제했습니다.","","success");
          this.resetDefault();
        });
    },
    addVacation() {
      const config = {
        headers: {
          Authorization: `Bearer ${this.access_token}`,
        },
      };
      this.newV.termS = this.newV.termS.idx;
      this.newV.usedS = this.newV.usedS.idx;
      this.axios.post(`${this.$store.state.BACKEND_URL}/api/vacation/write`,this.newV,config)
        .then(()=>{
          this.$alert("성공적으로 추가되었습니다.","","success");
          this.resetDefault();
        })
        .catch(()=>{
          this.$alert("실패했습니다.","","error");
        });
      this.newV.dialog = false;
    },
    closeD(){
      this.newV.dialog = false;
      this.resetAdd();
    },
    resetAdd() {
      this.newV.name = "";
      this.newV.type = 0;
      this.newV.day = "";
      this.newV.termS = {tag:"",idx:0};
      this.newV.usedS = {tag:"",idx:0};
    },
    all() {
      var count = 0;
      for(var i =0;i<this.vmp.length;i++){
          count += this.vmp[i].termS.idx;
      }
      return count;
    },
    use() {
      var count = 0;
      for(var i =0;i<this.vmp.length;i++){
          count += this.vmp[i].usedS.idx;
      }
      return count;
    },
    left() {
      return this.all()-this.use();
    },
    callVCInfo() {
      const config = {
        headers: {
          Authorization: `Bearer ${this.access_token}`,
        }
      };
      this.axios.get(`${this.$store.state.BACKEND_URL}/api/vacation/list`, config)
        .then((res)=>{
          this.vmp = res.data;
          for(let i = 0; i < this.vmp.length; i++){
            let tmp = this.vmp[i].termS;
            this.vmp[i].termS = {"tag":(tmp-1)+"박"+tmp+"일", "idx":tmp};
            tmp = this.vmp[i].usedS;
            this.vmp[i].usedS = {"tag":(tmp-1)+"박"+tmp+"일", "idx":tmp};
          }
          this.filterList(this.node);
        }).catch(()=>{
          this.$alert("예상치 못한 에러가 발생했습니다. 고객센터로 문의해 주세요.","","error");
        });
    },
    filterList(node) {
      if(node==99)  this.filterVmp = this.vmp;
      else this.filterVmp =  this.vmp.filter((item)=>{
        return item.type == node;
      })
      this.node = node;
    }
  },
  computed :{
    ...mapState(['isLogin', 'access_token'])
  },
  mounted() {
    if(!this.isLogin){
      this.$alert("로그인이 필요한 페이지입니다.","","warning");
      this.$router.push('/');
      return;
    } 
    this.node = 99;
    this.callVCInfo();
    this.makeTerm();
  }
}
</script>
<style>
</style>