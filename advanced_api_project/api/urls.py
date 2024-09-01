from django.urls import path
from .views import (
    BookListView, 
    BookCreateView, 
    BookRetrieveApiView,
    BookUpdateApiView,
    BookDestroyApiView
)

urlpatterns = [
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/create/", BookCreateView.as_view(), name="create_book"),
    path("books/details/", BookRetrieveApiView.as_view(), name="retrieve_book"),
    path("books/create/", BookUpdateApiView.as_view(), name="update_book"),
    path("books/create/", BookDestroyApiView.as_view(), name="destroy_book"),
]