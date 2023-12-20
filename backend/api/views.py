from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from .models import API

# Create your views here.

class ApiViewSet(viewsets.ModelViewSet):
    queryset = API.objects.all()
    serializer_class = serializers.ApiSerializer
    