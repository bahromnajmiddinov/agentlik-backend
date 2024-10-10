from django.urls import path

from .views import PollListView


urlpatterns = [
    path('', PollListView.as_view(), name='api_polls'),
]
