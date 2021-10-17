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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # user app and login related path
    path("api/user/", include("user.urls")),
    path('api/user/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/user/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/user/registration", include("dj_rest_auth.registration.urls")),
    # setting app path
    path("api/usersetting/", include("usersetting.urls")),
    # diary app path
    path("api/diary/", include("diary.urls")),
    # contest app path
    path("api/contest/", include("contest.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
