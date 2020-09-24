import django_filters
from django import forms
from .models import *


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    
    class Meta:
        model = Exam
        fields = ['year', 'board']