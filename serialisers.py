from rest_framework import serializers
from .models import DemonSlayer

class SlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemonSlayer
        fields = ['id', 'first_name', 'last_name', 'age', 'category', 'element_type']