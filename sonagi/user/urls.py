from django.urls import path
from .views import CurrentUserAPIView, google_login_redirect, google_login_callback, google_login_finish

urlpatterns = [
    path("user", CurrentUserAPIView.as_view(), name="current-user"),
    path("social-login/google", google_login_redirect, name="google-login-redirect"),
    path("social-login/google/callback", google_login_callback, name="google-login-callback"),
    path("social-login/google/login_finish", google_login_finish.as_view(), name="google-login-finish")

]