from .models import Contest
from .serializers import ContestListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ContestShowAllView(APIView):
    def get(self, request):
        serializer = ContestListSerializer(Contest.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContestShowBeforeView(APIView):
    def get(self, request):
        serializer = ContestListSerializer(Contest.objects.filter(contest_status="before"), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContestShowProgressView(APIView):
    def get(self, request):
        serializer = ContestListSerializer(Contest.objects.filter(contest_status="progress"), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContestShowEndView(APIView):
    def get(self, request):
        serializer = ContestListSerializer(Contest.objects.filter(contest_status="end"), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        