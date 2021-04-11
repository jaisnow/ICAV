from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=500, null=True, blank=True)
    authors = models.CharField(max_length=500, null=True, blank=True)
    isbn13 = models.CharField(max_length=500, null=True, blank=True)
    isbn10 = models.CharField(max_length=500, null=True, blank=True)
    price = models.CharField(max_length=500, null=True, blank=True)
    publisher = models.CharField(max_length=500, null=True, blank=True)
    pubyear = models.CharField(max_length=50)
    subjects = models.CharField(max_length=500, null=True, blank=True)
    lexile = models.CharField(max_length=500, null=True, blank=True)
    pages = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title