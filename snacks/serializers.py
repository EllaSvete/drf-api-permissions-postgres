from dataclasses import fields
from rest_framework import serializers
from .models import Snack

class SnackSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ("id", "description", "title", "created_at")
    model = Snack