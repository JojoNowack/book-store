import django_filters
from django_filters import DateFilter, CharFilter,NumberFilter
from django_filters import rest_framework as filters
from django_filters.filters import BooleanFilter

from .models import Articles

class booksFilter(django_filters.FilterSet):


    title = CharFilter(field_name='title',lookup_expr='icontains', label='Titel')
    year = NumberFilter(field_name='date',lookup_expr='gte',label='Herrausgabejahr')
    author = CharFilter(field_name='author',lookup_expr='icontains',label='Author')
    body = CharFilter(field_name='body',lookup_expr='icontains',label='nur verfügbar?')
    #isavailable = BooleanFilter(field_name='isavailable',label='s')

    class Meta:
        model = Articles
        fields = [
        ]
        