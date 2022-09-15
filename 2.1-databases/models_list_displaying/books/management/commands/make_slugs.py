from django.core.management.base import BaseCommand
from transliterate import slugify as tr_slugify
from django.template.defaultfilters import slugify as dj_slugify
from books.models import Book

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        books = Book.objects.all()

        for book in books:
            if tr_slugify(book.name) != None:
                book.slug = tr_slugify(book.name)
            elif dj_slugify(book.name) != None:
                book.slug = dj_slugify(book.name)
            book.save()