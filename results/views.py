from django.shortcuts import render
from django.views import generic
from .filters import UserFilter
from django_filters.views import FilterView
from .models import *

class Index(generic.TemplateView):

    template_name = 'index.html'


class Search(generic.ListView):
    template_name = 'checker.html'
    model = StudentInfo
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        user_list = StudentInfo.objects.all()

        user_filter = UserFilter(self.request.GET, queryset=user_list)
        context = {
            'filter': user_filter
        }
        return context
