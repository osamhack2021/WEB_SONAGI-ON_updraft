from .models import Contest
from .serializers import ContestListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework

# Create your views here.
class ContestListView(APIView):
    permission_classes = [rest_framework.permissions.AllowAny]
    def get(self, request):
        serializer = ContestListSerializer(Contest.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = ContestListSerializer(Contest.objects.filter(contest_status=request.data['contest_status']), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContestShowView(APIView):
    permission_classes = [rest_framework.permissions.AllowAny]
    def post(self, request):
        serializer = ContestListSerializer(Contest.objects.get(id=request.data['id']))
        return Response(serializer.data, status=status.HTTP_200_OK)