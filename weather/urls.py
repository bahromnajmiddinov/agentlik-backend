from django.urls import path

from .views import get_region_weather


urlpatterns = [
    path('', get_region_weather, name='api-weather'),
]
