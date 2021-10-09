from django.urls import path
from .views import UserSettingCreateView, UserSettingReviseView, UserSettingShowView

urlpatterns = [
    path("create/", UserSettingCreateView.as_view(), name="create-usersetting"),
    path("revise/", UserSettingReviseView.as_view(), name="revise-usersetting"),
    path("get/", UserSettingShowView.as_view(), name="get-usersetting")
]