from django.urls import path
from .views import BoardListView, PostShowView, PostListView, PostWriteView, PostRewriteView, PostDeleteView, CommentListView, CommentWriteView, CommentRewriteView, CommentDeleteView

urlpatterns = [
    path("board", BoardListView.as_view(), name="list-board"),
    path("post/show", PostShowView.as_view(), name="show-one-post"),
    path("post/list", PostListView.as_view(), name="list-post"),
    path("post/write", PostWriteView.as_view(), name="write-post"),
    path("post/rewrite", PostRewriteView.as_view(), name="rewrite-post"),
    path("post/delete", PostDeleteView.as_view(), name="delete-post"),
    path("comment/list", CommentListView.as_view(), name="list-comment"),
    path("comment/write", CommentWriteView.as_view(), name="write-comment"),
    path("comment/rewrite", CommentRewriteView.as_view(), name="rewrite-comment"),
    path("comment/delete", CommentDeleteView.as_view(), name="delete-comment"),
]