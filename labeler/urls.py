from django.urls import path

from .views import RootCategoryListView, SubCategoryListView, PageListView, PageDetailView


urlpatterns = [
    path('root-categories/', RootCategoryListView.as_view(), name='api_root_categories'),
    path('sub-categories/', SubCategoryListView.as_view(), name='api_sub_categories'),
    path('page/', PageListView.as_view(), name='api_pages'),
    path('page/<id>/', PageDetailView.as_view(), name='api_page'),
]
