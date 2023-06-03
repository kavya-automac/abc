from rest_framework import serializers
from .models import *
class ABCSerializer(serializers.ModelSerializer):
    class Meta:
        model=ABC
        fields = "__all__"