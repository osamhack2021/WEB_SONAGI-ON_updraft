<template>
    <div>
        <v-card class="group pa-2">
        <v-icon small style="margin-left:5px">home</v-icon>
        <v-breadcrumbs :items="bcLink"></v-breadcrumbs>
        </v-card>
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
                    <v-row>
                        <v-col>
                            <h4>댓글</h4> {{boardData.comments.length}}
                        </v-col>
                        <v-col align="right">
                            <v-btn link to="/community"><h4>목록</h4></v-btn>
                        </v-col>
                    </v-row>
                </div>
                <v-divider></v-divider>
                <div>
                    <v-card tile class="elevation-0 ma-4" style="min-height: 100px;">
                        <v-row class="mt-2">
                            <v-textarea
                            solo
                            auto-grow
                            name="comments"
                            label="댓글을 입력하세요."
                            background-color="grey lighten-3"
                            rows="4"
                            ></v-textarea>
                        </v-row>
                        <v-row>
                            <v-col align="right">
                                <v-btn>댓글 작성</v-btn>
                            </v-col>
                        </v-row>
                    </v-card>
                    <v-divider></v-divider>
                </div>
                <div v-for="(v, k) in boardData.comments" :key="k">
                    <v-card tile class="elevation-0 ma-4" style="min-height: 100px;">
                        <v-row>
                            <v-col class="ma-2 col-2 primary--text">{{v.class}} {{v.name}}</v-col>
                            <v-col class="ma-2 col-3 grey--text" align="left">
                                {{v.date}}
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col class="ma-3">{{v.contents}}</v-col>
                        </v-row>
                    </v-card>
                    <v-divider></v-divider>
                </div>
                <v-divider></v-divider>
                <v-row>
                    <v-col class="col-2">
                        <v-card flat class="pa-2" color="grey lighten-3" align="center">
                            <h4>이전 글</h4>
                        </v-card>
                    </v-col>
                    <v-col class="my-2">
                        [공지]게시판 이용 가이드
                    </v-col>
                    <v-col class="ma-2" align="right">2021/09/22</v-col>
                </v-row><v-divider></v-divider>
                <v-row>
                    <v-col class="col-2">
                        <v-card flat class="pa-2" color="grey lighten-3" align="center">
                            <h4>다음 글</h4>
                        </v-card>
                    </v-col>
                    <v-col class="my-2">
                        test3
                    </v-col>
                    <v-col class="ma-2" align="right">2021/09/26</v-col>
                </v-row>
                <v-divider></v-divider>
            </v-card>
        </v-card>
        </v-layout>
    </div>
</template>

<script>

export default {
    name: 'Post',
    data: ()=> ({
        bcLink: [
           {
             text: '대시보드',
             disabled: false,
             href: '/',
           },
           {
             text: '커뮤니티',
             disabled: false,
             href: 'community',
           },
         ],
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