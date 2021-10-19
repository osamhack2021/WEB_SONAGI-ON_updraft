from django.urls import path
from .views import VacationWriteView, VacationRewriteView, VacationDeleteView, VacationListView

urlpatterns = [
    path("write", VacationWriteView.as_view(), name="write-vacation"),
    path("rewrite", VacationRewriteView.as_view(), name="rewrite-vacation"),
    path("delete", VacationDeleteView.as_view(), name="delete-vacation"),
    path("list", VacationListView.as_view(), name="list-vacation")
]