from django.urls import path

from .views import ApealsStatistcsAPIView


urlpatterns = [
    path('statistcs/', ApealsStatistcsAPIView.as_view(), name='api_apeals_statistcs'),
]
