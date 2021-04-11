from .models import Books
from .serializers import BooksSerializer
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class BooksList(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    def get_queryset(self):
        number_of_rows = self.request.query_params.get('rows')
        if number_of_rows:
            try:
                n_row = int(number_of_rows)
                book_rows = Books.objects.all()[:n_row]
            except ValueError:
                book_rows = []
        else:
            book_rows = Books.objects.all()
        return book_rows


class FilterBooksList(APIView):
    """
    List all filter books according to column.
    """

    def get(self, request, *args, **kwargs):
        try:
            data = request.query_params
            converted_data = dict(zip(data.keys(), data.values()))
            filtered_data = Books.objects.filter(**converted_data)
            serializer = BooksSerializer(filtered_data, many=True)
            return Response(serializer.data)
        except Exception as e:
            error = {
                  "Failure": "Error", 
                  "Description": "column is not present in database"
             },
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
