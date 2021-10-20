from django.urls import path
from .views import UserSettingReviseView, UserSettingShowView

urlpatterns = [
    path("revise", UserSettingReviseView.as_view(), name="revise-usersetting"),
    path("get", UserSettingShowView.as_view(), name="get-usersetting")
]