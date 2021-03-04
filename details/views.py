from django.shortcuts import render

from rest_framework import viewsets
from .models import Students
from .serializers import StudentSerailizer


class StudentViewset(viewsets.ModelViewSet):
    queryset = Students.objects.all().order_by('-total_percentage')
    serializer_class =  StudentSerailizer