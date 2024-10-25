from rest_framework import serializers

from .models import Staff, Role, Url
from labeler.models import StaffsThroughTable


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    staff_set = serializers.HyperlinkedIdentityField(view_name='api_staff', read_only=True, lookup_field='id')

    class Meta:
        model = Role
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    urls = UrlSerializer(many=True, read_only=True)
    full_name = serializers.CharField(source='get_full_name')
    staff_set = StaffsThroughTable()
    
    class Meta:
        model = Staff
        fields = '__all__'
        extra_fields = ['full_name']
