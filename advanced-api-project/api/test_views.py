from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username="testuser", password="testpass")
        
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984", publication_year=1949, author=self.author
        )
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])

    def test_create_book(self):
        data = {'title': 'Animal Farm', 'publication_year': 1945, 'author': self.author.id}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_read_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], '1984')

    def test_update_book(self):
        data = {'title': '1984 - Updated', 'publication_year': 1950}
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, '1984 - Updated')

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        response = self.client.get(self.list_url, {'title': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_order_books(self):
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['results'][0]['publication_year'] <= response.data['results'][1]['publication_year'])
