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
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    #user.api의 모든 url 정보를 받아오는 path 설정 (include)
    path("api/", include("user.urls")),
    #path("api-auth/", include("rest_framework.urls")), 이건 필요없는듯
    #login, registration등 path 설정
    path("api/rest-auth/", include("rest_auth.urls")),
    # 토큰 발급 및 재발급 페이지 설정
    path('api/rest-auth/obtain_token/', obtain_jwt_token, name="obtain-jwt"),
    path('api/rest-auth/refresh_token/', refresh_jwt_token, name="refresh-jwt"),
    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),
]
