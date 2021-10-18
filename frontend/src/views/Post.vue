<template>
    <v-layout justify-center>
    <v-card class="pa-4 ma-4" style="width: 900px;">
        <v-card tile class="elevation-0">
            <v-toolbar flat color="grey lighten-3"><h2>{{boardData.title}}</h2></v-toolbar>
            <v-divider></v-divider>
            <v-row>
                <v-col class="ma-2"><h4>작성자</h4> : {{boardData.class}} {{boardData.name}}</v-col>
                <v-col class="ma-2" align="right">
                    <h4>작성일</h4> : {{boardData.date}}   <h4>조회수</h4> : {{boardData.views}}
                </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-card tile class="elevation-0 ma-2" style="min-height: 300px;">
                {{boardData.contents}}
            </v-card>
            <div class="ma-2">
                <h4>댓글</h4> {{boardData.comments.length}}
            </div>
            <v-divider></v-divider>
            <v-card tile class="elevation-0">
            </v-card>
            <v-divider></v-divider>
            <v-divider></v-divider>
            <v-divider></v-divider>
            <v-divider></v-divider>
            <v-divider></v-divider>
        </v-card>
    </v-card>
    </v-layout>
</template>

<script>

export default {
    name: 'Post',
    data: ()=> ({
        boardData:{
            title: "언제 전역 하냐",
            class: "상병",
            name: "정재훈",
            date: "2021-09-23 23:07:51",
            views: 10,
            contents: "ㅈㄱㄴ\n 아 빨리 전역하고 싶다.",
            comments: [
                {
                    class: "일병",
                    name: "국현호",
                    date: "2021-09-23 23:09:35",
                    contents: "저는 휴가라도 빨리 나가고 싶습니다...",
                },
                {
                    class: "일병",
                    name: "정우성",
                    date: "2021-09-23 23:10:47",
                    contents: "휴가 개꿀 ㅎ",
                },
            ],
        }
    }),
}
</script>

<style>
    h4 {display: inline;}
</style>