from rest_framework.permissions import IsAuthenticated
from .models import Api
from .serializers import ApiSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework import viewsets


class ApiList(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ApiSerializer
    queryset = Api.objects.all()
