from .models import UserSetting
from .serializers import UserSettingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.

class UserSettingReviseView(APIView):
    def post(self, request):
        # request : some of {"nickname", "major", "type", "enlisted_date", "delisted_date", "promotion1_date", "promotion2_date", "promotion3_date"}
        # permission : logined user  
        try:
            target = UserSetting.objects.get(email=request.user.email)
            serializer = UserSettingSerializer(target, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"result":"success"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({"detail":"잘못된 접근입니다."}, status=status.HTTP_403_FORBIDDEN)

class UserSettingShowView(APIView):
    def get(self, request):
        # request : just get
        # permission : logined user  
        try:
            target = UserSetting.objects.get(email=request.user.email)
            serializer = UserSettingSerializer(target)
            return Response(serializer.data)
        except:
            return JsonResponse({"detail":"잘못된 접근입니다."}, status=status.HTTP_403_FORBIDDEN)