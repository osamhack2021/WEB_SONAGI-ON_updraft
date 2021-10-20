from django.urls import path
from .views import ContestListView, ContestShowView

urlpatterns = [
    path("list", ContestListView.as_view(), name="list-contest"),
    path("show", ContestShowView.as_view(), name="show-one-contest")
]