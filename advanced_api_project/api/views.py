from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView,
    UpdateAPIView, 
    DestroyAPIView, 
    RetrieveAPIView
)
from .models import Book
from .serializers import BookSerializer
from rest_framework import serializers
import datetime
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)

        print(f"Book '{serializer.instance.title}' by {author.name} was created.")

class BookRetrieveApiView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateApiView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        # Custom update logic: Ensure publication year is not in the future
        publication_year = serializer.validated_data.get('publication_year')
        current_year = datetime.now().year
        if publication_year > current_year:
            raise ValidationError(f"Publication year {publication_year} cannot be in the future.")

        # Automatically set the last modified time (assuming you have a `modified_at` field in your model)
        serializer.save(modified_at=datetime.now())

        # Log the update action
        book = serializer.instance
        print(f"Book '{book.title}' by {book.author.name} was updated.")

class BookDestroyApiView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

