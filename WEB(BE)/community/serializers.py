from .models import Board, Post, Comment
from rest_framework import serializers
from usersetting.models import UserSetting

class BoardListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Board
        fields = '__all__'

class PostShowSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    image = serializers.ImageField(use_url=True)
    nickname = serializers.SerializerMethodField()
    prev_id = serializers.SerializerMethodField()
    next_id = serializers.SerializerMethodField()

    def get_nickname(self, obj):
        return obj.email.setting.get(email=obj.email.email).nickname

    def get_prev_id(self, obj):
        tmp = Post.objects.filter(board_id=obj.board_id, id__lt=obj.id)
        if len(tmp) > 0:
            return tmp[len(tmp)-1].id
        else:
            return
    
    def get_next_id(self, obj):
        tmp = Post.objects.filter(board_id=obj.board_id, id__gt=obj.id)
        if len(tmp) > 0:
            return tmp[0].id
        else:
            return

    class Meta:
        model = Post
        fields = ['id', 'prev_id', 'next_id', 'nickname', 'title', 'content', 'image', 'is_notice', 'write_date']

class PostListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    image = serializers.ImageField(use_url=True)
    nickname = serializers.SerializerMethodField()

    def get_nickname(self, obj):
        return obj.email.setting.get(email=obj.email.email).nickname

    class Meta:
        model = Post
        fields = ['id', 'nickname', 'title', 'image', 'is_notice', 'write_date']

class PostWriteSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False, allow_null=True)
    class Meta:
        model = Post
        fields = ['board_id', 'title', 'content', 'image']

class PostRewriteSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False, allow_null=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

class CommentListSerializer(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    def get_nickname(self, obj):
        return obj.email.setting.get(email=obj.email.email).nickname

    class Meta:
        model = Comment
        fields = ['id', 'nickname', 'content', 'write_date']

class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post_id', 'content']

class CommentRewriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']