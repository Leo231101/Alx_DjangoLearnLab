from rest_framework.generics import ListAPIView
from .models import Book  # Assuming your model is named Book
from .serializers import BookSerializer  # Assuming you have a corresponding serializer


#Create your views here.

class BookList(ListAPIView):
    queryset = Book.objects.all()  # This is the default queryset that will be used
    serializer_class = BookSerializer  # This serializer will be used to convert the data


