from rest_framework import serializers
from . import models


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.API
        fields = '__all__'
