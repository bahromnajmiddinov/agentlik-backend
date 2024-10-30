from rest_framework import serializers

from .models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['full_name', 'email', 'phone_number', 'address', 'work_address', 'position', 'title', 'text']
