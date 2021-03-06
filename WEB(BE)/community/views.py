from .models import Board, Post, Comment
from .serializers import BoardListSerializer, PostShowSerializer, PostListSerializer, PostWriteSerializer, PostRewriteSerializer, CommentListSerializer, CommentWriteSerializer, CommentRewriteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination
import rest_framework

class PostPageNumberPagination(PageNumberPagination):
    page_size = 10

class CommentPageNumberPagination(PageNumberPagination):
    page_size = 10

# Create your views here.

User = get_user_model()

class BoardListView(APIView):
    permission_classes = [rest_framework.permissions.AllowAny]
    def get(self, request):
        serializer = BoardListSerializer(Board.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostShowView(APIView):
    permission_classes = [rest_framework.permissions.AllowAny]
    def post(self, request):
        posts = Post.objects.get(id=request.data['id'])
        serializer = PostShowSerializer(posts)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostListView(APIView):
    permission_classes = [rest_framework.permissions.AllowAny]
    def post(self, request):
        paginator = PostPageNumberPagination()
        posts = Post.objects.filter(board_id=request.data['board_id'])
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostWriteView(APIView):
    def post(self, request):
        # request : {"board_id", "title", "content", "image"}
        # permission : logined user

        serializer = PostWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(email=User.objects.get(email=request.user.email))
            return JsonResponse({"result":"success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostRewriteView(APIView):
    def post(self, request):
        # request : {"id", "title", "content", "image"}
        # permission : logined user 
         
        cur_user = User.objects.get(email=request.user.email)
        try:
            target = cur_user.post.get(id=request.data['id'])
        except Post.DoesNotExist:
            return JsonResponse({'detail': '???????????? ???????????? ???????????? ????????????.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({'detail': '????????? ???????????????.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = PostRewriteSerializer(target, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"result":"success"}, status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDeleteView(APIView):
    def post(self, request):
        # request : {"id"}
        # permission : logined user 
             
        cur_user = User.objects.get(email=request.user.email)
        try:
            target = cur_user.post.get(id=request.data['id'])
        except Post.DoesNotExist:
            return JsonResponse({'detail': '???????????? ???????????? ???????????? ????????????.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({'detail': '????????? ???????????????.'}, status=status.HTTP_400_BAD_REQUEST)
        
        target.delete()
        return JsonResponse({"result":"success"}, status=status.HTTP_200_OK)



class CommentListView(APIView):
    permission_classes = [rest_framework.permissions.AllowAny]
    def post(self, request):
        paginator = CommentPageNumberPagination()
        posts = Comment.objects.filter(post_id=request.data['post_id'])
        serializer = CommentListSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CommentWriteView(APIView):
    def post(self, request):
        # request : {"post_id", "content"}
        # permission : logined user

        serializer = CommentWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(email=User.objects.get(email=request.user.email))
            return JsonResponse({"result":"success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentRewriteView(APIView):
    def post(self, request):
        # request : {"id", "content"}
        # permission : logined user 
         
        cur_user = User.objects.get(email=request.user.email)
        try:
            target = cur_user.comment.get(id=request.data['id'])
        except Comment.DoesNotExist:
            return JsonResponse({'detail': '???????????? ????????? ???????????? ????????????.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({'detail': '????????? ???????????????.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CommentRewriteSerializer(target, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"result":"success"}, status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDeleteView(APIView):
    def post(self, request):
        # request : {"id"}
        # permission : logined user 
             
        cur_user = User.objects.get(email=request.user.email)
        try:
            target = cur_user.comment.get(id=request.data['id'])
        except Comment.DoesNotExist:
            return JsonResponse({'detail': '???????????? ????????? ???????????? ????????????.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({'detail': '????????? ???????????????.'}, status=status.HTTP_400_BAD_REQUEST)
        
        target.delete()
        return JsonResponse({"result":"success"}, status=status.HTTP_200_OK)