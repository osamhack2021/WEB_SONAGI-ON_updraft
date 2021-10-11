<template lang="">
    <v-layout align-center justify-center row fill-height class="py-8 px-4">
        <v-card class="py-8 px-4 ma-4" style="max-width: 900px; width: 900px; height: 700px">
            <v-text-field
            v-model="message1"
            label="제목"
            clearable
          ></v-text-field>
                <v-textarea
                counter
                label="내용"
                :rules="rules"
                :value="value"
                rows="15"
                row-height="30"
                ></v-textarea>
        </v-card>
    </v-layout>
</template>
<script>
export default {
    
}
</script>
<style lang="">
    
</style>