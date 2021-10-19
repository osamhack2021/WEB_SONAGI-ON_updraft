from .models import Diary
from .serializers import DiarySearchSerializer, DiaryWriteSerializer, DiaryListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class DiaryWriteView(APIView):
    def post(self, request):
        # request : {"title", "content", "emotion"}
        # permission : logined user

        serializer = DiaryWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(email=User.objects.get(email=request.user.email))
            return JsonResponse({"result":"success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiaryRewriteView(APIView):
    def post(self, request):
        # request : {"id", "title", "content", "emotion"}
        # permission : logined user 
         
        cur_user = User.objects.get(email=request.user.email)
        try:
            target = cur_user.diary.get(id=request.data['id'])
        except Diary.DoesNotExist:
            return JsonResponse({'detail': '해당하는 일기가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({'detail': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = DiaryWriteSerializer(target, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"result":"success"}, status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiaryDeleteView(APIView):
    def post(self, request):
        # request : {"id"}
        # permission : logined user 
             
        cur_user = User.objects.get(email=request.user.email)
        try:
            target = cur_user.diary.get(id=request.data['id'])
        except Diary.DoesNotExist:
            return JsonResponse({'detail': '해당하는 일기가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({'detail': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        target.delete()
        return JsonResponse({"result":"success"}, status=status.HTTP_200_OK)

class DiaryListView(APIView):
    def get(self, request):
        # request : nothing
        # permission : logined user      
        
        cur_user = User.objects.get(email=request.user.email)
        target = cur_user.diary.filter(email=request.user.email)
        serializer = DiaryListSerializer(target, many=True)
        return Response(serializer.data)

    def post(self, request):
        # request : {"start_date", "end_date", "search", "emotion"} 
        # !! emotion should be blank or in emotion_choices in diary/models.py
        # permission : logined user 

        cur_user = User.objects.get(email=request.user.email)

        serializer = DiarySearchSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        validated_data = serializer.validated_data
        target = cur_user.diary.filter(Q(title__icontains=validated_data['search']) | Q(content__icontains=validated_data['search']),
                                        write_date__range=[validated_data['start_date'], validated_data['end_date']],
                                        emotion__icontains=validated_data['emotion'])
        
        serializer = DiaryListSerializer(target, many=True)
        return Response(serializer.data)

class DiaryShowView(APIView):
    def post(self, request):
        cur_user = User.objects.get(email=request.user.email)
        try:
            target = cur_user.diary.get(id=request.data['id'])
            serializer = DiaryListSerializer(target)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Diary.DoesNotExist:
            return JsonResponse({'detail': '해당하는 일기가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({'detail': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)