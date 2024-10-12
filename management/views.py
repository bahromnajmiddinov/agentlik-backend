from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Role, Staff
from .serializers import RoleSerializer, StaffSerializer


class StaffListView(ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffDetailView(RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    lookup_field = 'id'


class RoleListView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetailView(RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    lookup_field = 'id'
