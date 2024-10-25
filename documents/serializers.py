from rest_framework import serializers

from .models import Document, DocumentCategory, SimpleDocument


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = '__all__'
        

class DocumentSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Document
        fields = '__all__'


class SimpleDocumentSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = SimpleDocument
        fields = '__all_-'

