import django_filters
from django_filters.filters import DateFilter

from .models import Book

class booksFilter(django_filters.FilterSet):
    new_author = django_filters.CharFilter(field_name='author')
    class Meta:
        model = Book
        fields = [
            'title',
            # 'body',
            # 'date',
            'new_author',
        ]