from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

class Home(TemplateView):
    template_name = "index.html"
