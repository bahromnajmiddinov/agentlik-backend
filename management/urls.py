from django.urls import path

from .views import StaffListView, StaffDetailView, RoleListView, RoleDetailView


urlpatterns = [
    path('staffs/', StaffListView.as_view(), name='api_staffs'),
    path('staffs/<id>/', StaffDetailView.as_view(), name='api_staff'),
    path('roles/', RoleListView.as_view(), name='api_roles'),
    path('roles/<id>', RoleDetailView.as_view(), name='api_role'),
]
