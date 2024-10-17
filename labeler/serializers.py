from rest_framework import serializers

from .models import RootCategory, SubCategory, Page
from news.serializers import NewSerializer
from documents.serializers import DocumentSerializer
from polls.serializers import PollSerializer
from management.serializers import StaffSerializer


class PageSerializer(serializers.ModelSerializer):
    news = NewSerializer(many=True, read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)
    staffs = StaffSerializer(many=True, read_only=True)
    polls = PollSerializer(many=True, read_only=True)

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
