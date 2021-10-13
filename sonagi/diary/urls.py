from django.urls import path
from .views import DiaryWriteView, DiaryRewriteView, DiaryDeleteView, DiaryListView

urlpatterns = [
    path("write", DiaryWriteView.as_view(), name="write-diary"),
    path("rewrite", DiaryRewriteView.as_view(), name="rewrite-diary"),
    path("delete", DiaryDeleteView.as_view(), name="delete-diary"),
    path("list", DiaryListView.as_view(), name="list-diary"),
]