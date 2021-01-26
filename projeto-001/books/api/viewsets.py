from rest_framework import viewsets
from books.api.serializers import BooksSerializer
from books.models import Book


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
