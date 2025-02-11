from rest_framework import serializers

from .models import *


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
