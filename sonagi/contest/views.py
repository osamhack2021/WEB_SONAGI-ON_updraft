from .models import Contest
from .serializers import ContestListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ContestListView(APIView):
    def post(self, request):
        serializer = ContestListSerializer(Contest.objects.filter(contest_status=request.data['contest_status']), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContestShowView(APIView):
    def post(self, request):
        serializer = ContestListSerializer(Contest.objects.get(id=request.data['id']))
        return Response(serializer.data, status=status.HTTP_200_OK)