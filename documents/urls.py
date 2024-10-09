from django.urls import path

from .views import DocumentListView, DocumentDetailView, CategoryListView


urlpatterns = [
    path('', DocumentListView.as_view(), name='api_documents'),
    path('<id>', DocumentDetailView.as_view(), name='api_document'),
    path('categories/', CategoryListView.as_view(), name='api_documents_categories'),
]
