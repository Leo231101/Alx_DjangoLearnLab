from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer

# List view for Authors, including nested books
class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
