from django.urls import path
from .views import ContestShowAllView, ContestShowBeforeView, ContestShowProgressView, ContestShowEndView

urlpatterns = [
    path("all", ContestShowAllView.as_view(), name="list-contest"),
    path("before", ContestShowBeforeView.as_view(), name="list-contest"),
    path("progress", ContestShowProgressView.as_view(), name="list-contest"),
    path("end", ContestShowEndView.as_view(), name="list-contest"),
]