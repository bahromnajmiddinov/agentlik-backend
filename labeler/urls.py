from django.urls import path

from .views import RootCategoryListView, SubCategoryListView


urlpatterns = [
    path('root-categories/', RootCategoryListView.as_view(), name='api_root_categories'),
    path('sub-categories/', SubCategoryListView.as_view(), name='api_sub_categories'),
]
