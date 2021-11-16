import django_filters

from .models import Articles

class booksFilter(django_filters.FilterSet):

    class Meta:
        model = Articles
        fields = [
            'title',
            'body',
            'date',
            'author',
        ]