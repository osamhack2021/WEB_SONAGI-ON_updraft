<template>
            <v-sheet
              max-width="700"
            >
              <v-slide-group
                mandantory
                show-arrows
                v-model="model"
              >
                <v-slide-item
                    v-for="i in emotions" :key="i"
                    v-slot="{ active, toggle }"
                >
                  <v-btn
                    class="mx-4"
                    @click="toggle"
                    large
                    icon
                    depressed
                    rounded
                    :input-value="active"
                    active-class="indigo darken-3 white--text"
                  >
                    <v-icon>{{i}}</v-icon>
                  </v-btn>
                </v-slide-item>
              </v-slide-group>
            </v-sheet>
</template>

<script>

    
export default {
    data:()=>({
        model: null,
        
        emotions: [
        'mdi-emoticon-excited-outline',
        'mdi-emoticon-cool-outline',
        'mdi-emoticon-neutral-outline',
        'mdi-emoticon-confused-outline',
        'mdi-emoticon-angry-outline',
        'mdi-emoticon-sad-outline',
        'mdi-emoticon-sick-outline',
        'mdi-emoticon-cry-outline',
        'mdi-emoticon-dead-outline',
        ],
    }),
    watch: {
      model: function(){
        console.log(this.model);
      }
    }
}
</script>