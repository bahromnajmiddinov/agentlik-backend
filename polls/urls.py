from django.urls import path

from .views import PollListView, PollDetailView


urlpatterns = [
    path('', PollListView.as_view(), name='api_polls'),
    path('<id>', PollDetailView.as_view(), name='api_poll'),
]
