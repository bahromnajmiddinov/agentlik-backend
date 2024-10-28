from rest_framework import serializers

from .models import RootCategory, SubCategory, Page, CustomTable, CustomTableField, PageImage
from news.serializers import NewSerializer
from documents.serializers import DocumentSerializer, SimpleDocumentSerializer
from polls.serializers import PollSerializer
from management.serializers import StaffSerializer


class CustomTableFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomTableField
        fields = '__all__'


class CustomTableSerializer(serializers.ModelSerializer):
    customtablefield_set = CustomTableFieldSerializer(many=True, read_only=True)

    class Meta:
        model = CustomTable
        fields = '__all__'


class PageImageSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageImage
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    table = CustomTableSerializer(many=True, read_only=True)
    news = NewSerializer(many=True, read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)
    simple_documents = SimpleDocumentSerializer(many=True, read_only=True)
    staffs = StaffSerializer(many=True, read_only=True)
    polls = PollSerializer(many=True, read_only=True)
    pageimage_set = PageImageSetSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    pages = PageSerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = '__all__'


class RootCategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True)

    class Meta:
        model = RootCategory
        fields = '__all__'
