from django.shortcuts import render
from .models import User,Status,Personnel_information,request_position,Criterion
from rest_framework import viewsets
from .serializers import Userserializer,StatusSerializer, Personnel_informationserializer, request_positionserializer, Criterionserializer

# Create your views here
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class Personnel_informationViewset(viewsets.ModelViewSet):
    queryset = Personnel_information.objects.all()
    serializer_class = Personnel_informationserializer

class request_positionViewset(viewsets.ModelViewSet):
    queryset = request_position.objects.all()
    serializer_class = request_positionserializer

class CriterionViewset(viewsets.ModelViewSet):
    queryset = Criterion.objects.all()
    serializer_class = Criterion.objects.all()
