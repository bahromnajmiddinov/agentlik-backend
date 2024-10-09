from django.urls import path

from .views import NewListView, NewDetailView, CategoryListView


urlpatterns = [
    path('', NewListView.as_view(), name='api_news'),
    path('<id>', NewDetailView.as_view(), name='api_new'),
    path('categories/', CategoryListView.as_view(), name='api_news_categories'),
]
