"""sonagi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    #user.urls의 모든 url 정보를 받아오는 path 설정 (include)
    path("api/user/", include("user.urls")),
    # 토큰 발급 및 재발급 페이지 설정
    path('api/rest-auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/rest-auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    # 소셜 로그인 페이지 설정
]
