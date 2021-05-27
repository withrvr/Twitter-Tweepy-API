from django.shortcuts import render
from django.views.generic import TemplateView


class Home_View(TemplateView):
    template_name = 'Home_Template.html'
