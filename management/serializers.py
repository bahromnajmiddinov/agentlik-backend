from rest_framework import serializers

from .models import Staff, Role


class RoleSerializer(serializers.ModelSerializer):
    staff_set = serializers.HyperlinkedIdentityField(view_name='api_staff', read_only=True, lookup_field='id')

    class Meta:
        model = Role
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)

    class Meta:
        model = Staff
        fields = '__all__'
