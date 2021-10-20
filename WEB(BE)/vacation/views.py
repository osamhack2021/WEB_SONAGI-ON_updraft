from .models import Vacation
from .serializers import VactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class VacationWriteView(APIView):
    def post(self, request):
        # request : {"name", "type", "day", "termS", "usedS"}
        # permission : logined user

        serializer = VactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(email=User.objects.get(email=request.user.email))
            return JsonResponse({"result":"success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VacationRewriteView(APIView):
    def post(self, request):
        # request : {"id", "name", "type", "day", "termS", "usedS"}
        # permission : logined user 
         
        cur_user = User.objects.get(email=request.user.email)
        try:
            target = cur_user.vacation.get(id=request.data['id'])
        except Vacation.DoesNotExist:
            return JsonResponse({'detail': '해당하는 휴가가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({'detail': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = VactionSerializer(target, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"result":"success"}, status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VacationDeleteView(APIView):
    def post(self, request):
        # request : {"id"}
        # permission : logined user 
             
        cur_user = User.objects.get(email=request.user.email)
        try:
            target = cur_user.vacation.get(id=request.data['id'])
        except Vacation.DoesNotExist:
            return JsonResponse({'detail': '해당하는 휴가가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({'detail': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        target.delete()
        return JsonResponse({"result":"success"}, status=status.HTTP_200_OK)

class VacationListView(APIView):
    def get(self, request):
        # request : nothing
        # permission : logined user      
        
        cur_user = User.objects.get(email=request.user.email)
        target = cur_user.vacation.filter(email=request.user.email)
        serializer = VactionSerializer(target, many=True)
        return Response(serializer.data)