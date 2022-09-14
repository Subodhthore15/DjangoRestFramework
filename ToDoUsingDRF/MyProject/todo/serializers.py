from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Todo
from rest_framework import serializers

class TodoSerializer(ModelSerializer):
    id= serializers.ReadOnlyField()
    class Meta:
        model = Todo
        fields="__all__"