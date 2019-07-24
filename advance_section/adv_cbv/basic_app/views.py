
from . import models

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView

# Create your views here.

# Basic variant (without cbv)
# def index(request):
#    return render(request, 'index.html')


# Variant with cbv
class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'Basic Injection!'
        return context


class SchoolListView(ListView):
    context_object_name = 'school_list'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    template_name = 'basic_app/school_detail.html'
    model = models.School
