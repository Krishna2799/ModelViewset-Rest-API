from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Operations


class OperationsSerializer(ModelSerializer):
    class Meta:
        model = Operations
        fields = '__all__'
