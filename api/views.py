from django.shortcuts import render
from .models import Students
from .serializers import StudentSerializer
from rest_framework import viewsets, permissions, parsers


class StudentViewSet(viewsets.ModelViewSet):
    """
    This API is open source API.
    You don't need any token here.And You can get, post, put, patch, delete freely this API
    """
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.AllowAny, ) 

        

class StudentInfosViewSet(viewsets.ModelViewSet):
    """
        This API is secured with authorization here.
        You need to login and send your token in header with `Authorization`
    """
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated, ) 


