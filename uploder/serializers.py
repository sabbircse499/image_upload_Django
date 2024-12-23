from rest_framework import serializers
from .models import product

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['id','title', 'image', 'description','price','newprice','discount', 'uploaded_at']