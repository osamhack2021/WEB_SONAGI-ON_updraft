from .models import Board, Post, Comment
from rest_framework import serializers

class BoardListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Board
        fields = '__all__'

class PostShowSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Post
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Post
        fields = ['id', 'email', 'title', 'image', 'is_notice', 'write_date']

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
    class Meta:
        model = Comment
        fields = '__all__'

class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post_id', 'content']

class CommentRewriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']