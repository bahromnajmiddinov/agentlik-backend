from rest_framework import serializers

from .models import New, NewCategory, NewImage


class NewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewImage
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCategory
        fields = '__all__'


class NewSerializer(serializers.ModelSerializer):
    images = NewImageSerializer(many=True, read_only=True)
    category_set = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = New
        fields = '__all__'
