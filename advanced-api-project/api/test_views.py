from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book

# Dummy data for testing
book_data = {
    "title": "Test Book",
    "author": "Author Name",
    "description": "A description of the book",
    "isbn": "1234567890",
    "published": "2022-01-01"
}

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        # Force authenticate the user for all test requests
        self.client.force_authenticate(user=self.user)

        # Create a few books for testing
        self.book1 = Book.objects.create(title="Book 1", author="Author 1", isbn="1111111111")
        self.book2 = Book.objects.create(title="Book 2", author="Author 2", isbn="2222222222")
        self.book3 = Book.objects.create(title="Book 3", author="Author 3", isbn="3333333333")

    def tearDown(self):
        # Remove authentication after each test case
        self.client.force_authenticate(user=None)

    def test_create_book(self):
        url = reverse('book-list')  # Assuming you are using a router for your URLs
        response = self.client.post(url, book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], book_data['title'])

    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        updated_data = {
            "title": "Updated Book 1",
            "author": "Updated Author 1",
            "isbn": "1111111111"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verify that the book is actually deleted
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_books_by_author(self):
        url = reverse('book-list') + '?author=Author 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book by Author 1

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Book'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # All books contain 'Book' in the title

    def test_order_books_by_title(self):
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, ["Book 1", "Book 2", "Book 3"])

    def test_unauthenticated_access(self):
        # Remove authentication
        self.client.force_authenticate(user=None)
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

