import django_filters
from django import forms
from .models import *


# class UserFilter(django_filters.FilterSet):
#     roll = django_filters.NumberFilter()
    
#     class Meta:
#         model = StudentInfo
#         fields = ['name', 'board', 'group', 'exam']



class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='exact')
    
    class Meta:
        model = StudentInfo
        fields = ['name', 'board', 'group', 'exam', 'roll']
