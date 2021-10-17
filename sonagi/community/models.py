from django.db import models
from django.utils import timezone
from sonagi.utils import RandomFileName

# Create your models here.
# 다음과 같은 계층적 구조를 이룬다.
#  Board1     Board 2
#    |           |
#   /  \        /  \
# Post1 Post2 Post3 Post4
#        |
#       / -------|--------|
#    Comment1 Comment2 Comment3

# 게시판을 저장해 두는 모델
class Board(models.Model):
    name = models.CharField(verbose_name="게시판 이름", max_length=20, null=False)

    def __str__(self):
        return self.name

# 게시글을 저장해 두는 모델
class Post(models.Model):
    board_id = models.ForeignKey(Board, related_name="post", on_delete=models.CASCADE, db_column="board_id")
    email = models.ForeignKey("user.User", related_name="post", to_field="email", on_delete=models.CASCADE, db_column="email")
    title = models.CharField(verbose_name="제목", max_length=100, null=False)
    content = models.CharField(verbose_name="내용", max_length=2000, null=True)
    image = models.ImageField(verbose_name="게시글 이미지", upload_to=RandomFileName("postimage"), blank=True)
    is_notice = models.BooleanField(verbose_name="공지사항 여부", default=False)
    write_date = models.DateTimeField(verbose_name="작성 일자", default=timezone.now)
    rewrite_date = models.DateTimeField(verbose_name="최종 수정 일자", auto_now=True)

    def __str__(self):
        return self.title


# 댓글을 저장해 두는 모델
class Comment(models.Model):
    post_id = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE, db_column="post_id")
    email = models.ForeignKey("user.User", related_name="comment", to_field="email", on_delete=models.CASCADE, db_column="email")
    content = models.CharField(verbose_name="내용", max_length=2000, null=True)
    write_date = models.DateTimeField(verbose_name="작성 일자", default=timezone.now)
    rewrite_date = models.DateTimeField(verbose_name="최종 수정 일자", auto_now=True)

    def __str__(self):
        return self.content