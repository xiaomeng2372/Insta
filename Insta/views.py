from django.shortcuts import render
from django.views.generic import TemplateView 
# Create your views here.
# when you send me a request, i want to render text html

class HelloWorld(TemplateView):
    template_name = 'test.html'