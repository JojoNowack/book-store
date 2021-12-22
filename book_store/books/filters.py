
import django_filters
from django_filters import DateFilter, CharFilter,NumberFilter
from django_filters import rest_framework as filters
from django_filters.filters import BooleanFilter, ChoiceFilter
from .models import Book, Category


def get_current_genre(request):
     genrerq = request.GET['genre']
     return genrerq

class booksFilter(django_filters.FilterSet):
    BOOKS_CHOICES = {
        ('', 'Alle Bücher'),
        ('True', 'verfügbare Bücher'),
        ('False', 'nicht verfügbare Bücher')
    }
    BOOLEAN_CHOICES = (('false', 'False'), ('true', 'True'),)

    title = CharFilter(field_name='title',lookup_expr='icontains', label='Buchtitel')
    year = NumberFilter(field_name='year',lookup_expr='icontains',label='Herrausgabejahr',min_value=1900, max_value=2100)
    author = CharFilter(field_name='book_author',label='Autor',lookup_expr='icontains')
    isavailable = ChoiceFilter(field_name='isavailable', lookup_expr='exact', choices=BOOKS_CHOICES,label='Was möchtest du sehen?')

    class Meta:
        model = Book
        fields = [
        ]

class booksFilterwithGenre(django_filters.FilterSet):
    BOOKS_CHOICES = {
        ('', 'Alle Bücher'),
        ('True', 'verfügbare Bücher'),
        ('False', 'nicht verfügbare Bücher')
    }

    all_categories = Category.objects.all()
    max_category = Category.objects.count()
    for x in range(0,max_category):
     globals()['cat%s' % x] = all_categories[x].genre
     globals()['catid%s' % x] = all_categories[x].id
    CAT_CHOICES = [
        (globals()['catid%s' % i],globals()['cat%s' % i]) for i in range(0,max_category)
    ]   

    GENRE_CHOICES = {
        ('Fantasy', 'Fantasy'),
        ('Thriller', 'Thriller'),
        ('Roman', 'Roman'),
        ('Kinderbuch', 'Kinderbuch'),
    }
    title = CharFilter(field_name='title',lookup_expr='icontains', label='Buchtitel')
    year = NumberFilter(field_name='year',lookup_expr='icontains',label='Herrausgabejahr',min_value=1900, max_value=2100)
    author = CharFilter(field_name='book_author',label='Autor',lookup_expr='icontains')
    genre = ChoiceFilter(field_name='genre',label='Genre',choices=CAT_CHOICES)
    #isavailable = ChoiceFilter(field_name='isavailable', lookup_expr='exact', choices=BOOKS_CHOICES, empty_label=get_current_genre,label='Was möchtest du sehen?')

    class Meta:
        model = Book
        fields = [
        ]



