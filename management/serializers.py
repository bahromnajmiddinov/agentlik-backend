from rest_framework import serializers

from .models import Staff, Role, Url


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
    get_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = '__all__'

    def get_full_name(self, obj):
        return obj.get_full_name
