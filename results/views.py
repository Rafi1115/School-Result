from django.shortcuts import render
from django.views import generic
from .filters import UserFilter
from .models import *

class Index(generic.TemplateView):

    template_name = 'index.html'


class Search(generic.TemplateView):
    template_name = 'index.html'
    model = Exam

    def get_context_data(self, *args, **kwargs):
        user_list = Exam.objects.all()
        user_filter = UserFilter(self.request.GET, queryset=user_list)
        context = {
            'filter': user_filter
        }
        return context
    