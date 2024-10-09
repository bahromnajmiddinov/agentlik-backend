from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Document, DocumentCategory
from .serializers import DocumentSerializer, CategorySerializer


class DocumentListView(ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentDetailView(RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    lookup_field = 'id'


class CategoryListView(ListAPIView):
    queryset = DocumentCategory.objects.all()
    serializer_class = CategorySerializer
