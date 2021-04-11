from rest_framework import serializers
from .models import Books


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'authors', 'isbn13', 
    			  'isbn10', 'price', 'publisher', 'pubyear',
    			  'subjects', 'lexile', 'pages', 'dimensions']