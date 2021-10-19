from django.urls import path
from .views import UserShowView #google_login_redirect, UserGoogleLoginView, UserGoogleCallbackView

urlpatterns = [
    path("user", UserShowView.as_view(), name="current-user"),
    #path("social-login/google", google_login_redirect, name="google-login-redirect"),
    #path("social-login/google/callback", UserGoogleLoginView, name="google-login-callback"),
    #path("social-login/google/login_finish", UserGoogleLoginView, name="google-login-finish")

]