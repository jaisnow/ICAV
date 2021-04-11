from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BooksList.as_view()),
    path('books/filter', views.FilterBooksList.as_view()),
]