# SONAGI-ON_상승기류

<img src="https://user-images.githubusercontent.com/33975225/133041510-963cf607-cd95-4348-b23b-7ad0da769835.png" alt="updraft2" style="zoom: 10%;" />

## 프로잭트 소개

- 기존 군에서는 소중한 나의 일기(소나기) 라는 군 생활 플래너를 장병들에게 제공 해오고 있습니다. 이는 단순한 일기장을 넘어서 자신의 군 생활에 대한 계획을 세우고, 이를 효과적으로 이끌어 나갈 수 있도록 도와주는 역할을 해 왔습니다. 하지만 현대 사회로 접어들면서, 이러한 아날로그 방식 보다는 스마트폰을 활용해 자신의 계획을 수립하고 기록을 남기는 사람들이 늘어났습니다. 군에서도 이에 발 맞춰, 스마트폰 보급이라는 사업의 효과성을 증대하기 위해 군 생활 플래너를 온라인 서비스로 제공하는 것을 제안합니다.



## 기능 설명

- 군 생활에 대한 계획 작성 가능, 자신이 군 생활을 하면서 느꼈던 점을 기록 가능, 공모전과 E러닝등 미래 설계를 위한 정보 공유, 자신이 작성해온 소나기 공유 등의 기능을 포함한 웹사이트 입니다.

- 기능

1. 대시보드
   - 전역일 계산기, 일기 작성 통계, 작은 캘린더 등 자주 사용하는 기능들에 바로 접근할 수 있는 메인 페이지입니다.
3. 일기장 
   - 일기를 작성하고, 자신이 작성한 일기들을 한 눈에 볼 수 있는 탭 입니다.
   - 하루하루 체력이 얼마나 늘었는지 스스로 체크하면서 발전한 모습을 확인할 수 있는 기능입니다.
5. 캘린더
   - 자신의 일정, 계획을 작성 하고 이를 쉽게 관리할 수 있는 페이지 입니다.
6. 커뮤니티 
   - 자유게시판, 질문 게시판 등 군인들만을 위한 게시판을 이용 가능한 페이지입니다.
7. 공모전/행사 
   - 군 내에서도 참여할 수 있는 다양한 공모전과 행사 정보들을 실시간으로 알려주는 페이지입니다.
8. 휴가 관리
   -  군 생활의 꽃, 휴가를 손쉽게 관리할 수 있는 페이지입니다.





## 기대 효과 및 전망

일반 플래너와 소나기의 차이점은 군 장병에게 최적화 되어 있다는 것입니다. 

대학 생활 정보를 알려주는 에브리타임, 일반적인 계획 수립에 도움을 주는 다양한 플래너 앱들은 군대 밖의 사회에서 유용합니다.

군 장병을 대상으로 하는 웹 사이트를 목표로 하고 있는 만큼 군 생활에 실질적으로 도움이 되는 기능들로 채워져 있습니다.

소나기On을 통해 장병들이 군 생활에 더욱 보람을 느끼고, 전역 이후의 삶을 위해 자신만의 일주를 하는데 도움을 줄 수 있을 것입니다. 

또한, 스마트폰 보급이 점차 확대되는 와중에 이를 적절히 활용할 수 있는 군 장병 대상 웹 사이트를 출시하는 것은 대내적으로나, 대외적으로나 크나큰 도움이 되리라 생각합니다.



## 컴퓨터 구성 / 필수 조건 안내 (Prerequisites)

```
Python >= 3.0
Django == 2.2.4
dj-rest-auth == 2.1.11
django-allauth == 0.45.0
django-rest-framework >= 3.12.0
django-cors-headers == 3.10.0
djangorestframework-simplejwt == 5.0.0

Nodejs >= 14.18.0
```



## 기술 스택 (Technique Used) 

### Back-End

 -  django
 -  django rest framework
 -  django allauth
 -  django simplejwt
 -  django cors header

### Front-End
 -  Vue.js CLI
 -  Vuetify
 -  Vuex
 -  Vue Router
 -  Axios
 -  Vuex-persistent
 -  vue animatednumbers
 -  vue chart.js
 -  vue alert

-----------------------------------------------------------이하 추가 작성 예정-------------------------------------------------

## 설치 안내 (Installation Process)

```bash
$ git clone https://github.com/osamhack2021/WEB_SONAGI-ON_updraft
```

### Back-End
```bash
$ cd sonagi
$ python manage.py makemigrations community contest diary user usersetting vacation
$ python manage.py migrate
$ python manage.py createsuperuser # create super user account
$ python manage.py runserver 0.0.0.0:[PORT]
```

### Front-End
```bash
$ cd frontend
$ npm install
$ npm run serve
```


## 프로젝트 사용법 (Getting Started)

### Back-End

/sonagi/sonagi 폴더에 secret.json이 필요합니다.
```
# secret.json
{
    "SECRET_KEY" : "[Personal_Secret_Key]",
    "STATE" : "[Personal_State]",
    "BASE_URL" : "[자신이 백엔드에서 사용할 URL]"
} 
```

다음으로 /sonagi/sonagi/settings.py의 CORS_ORIGIN_WHITELIST를 다음과 같이 바꿔야 합니다.
```
CORS_ORIGIN_WHITELIST = [
    "[프론트엔드 URL]"
]
```
url은 http 또는 https로 시작하여, 슬래쉬(/) 없이 끝나야 합니다.


### Front-End

frontend/src/store/index.js에서 Vuex의 state를 다음과 같이 바꿔야 합니다.
```
export default new Vuex.Store({
  ...
  state: {
    BACKEND_URL : '[자신의 백엔드 서버 URL]',
    isLogin: false,
    userdata: {},
    access_token: "",
    refresh_token: "",
  },
  ...
});
```

이러면 프로젝트를 사용할 준비가 끝납니다.


## 팀 정보 (Team Information)

- Jeong Jae hoon (jjh8501@gmail.com), Github Id: revlr
- kook hyun ho (kookhh0827@gmail.com), Github Id: kookhh0827
- Lee hyun su (masterpug99@gmail.com), Github Id: masterpug99



## 저작권 및 사용권 정보 (Copyleft / End User License)

 * [MIT](https://github.com/osam2020-WEB/Sample-ProjectName-TeamName/blob/master/license.md)

This project is licensed under the terms of the MIT license.
