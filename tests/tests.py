from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Books

class BooksListTests(APITestCase):

    def test_books_listing(self):
        """
        test for books listing method.
        """
        url = 'http://localhost:8000/tests/books/?rows=2'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class FilterBookListTests(APITestCase):

    def test_filter_query_with_correct_url(self):

        url = 'http://localhost:8000/tests/books/filter?author=Sapphire'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_filter_query_with_incorrect_url(self):

        url = 'http://localhost:8000/tests/books/filter?sfggdfsf=vbcvb'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
