from rest_framework import serializers

from .models import Phons

class PhonsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'admin_name', 'title_model', 'price', 'Processor', 'RAM' , 'Storage' ,'Display', 'Camera')
        model = Phons
