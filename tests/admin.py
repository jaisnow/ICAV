from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Books


class BookResource(resources.ModelResource):

    class Meta:
        model = Books


class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

    list_display = ['title', 'author', 'authors', 'isbn13', 
    				'isbn10', 'price', 'publisher', 'pubyear',
    				'subjects', 'lexile', 'pages', 'dimensions']

admin.site.register(Books, BookAdmin)

