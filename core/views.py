from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView,TemplateView
from .models import *


class HomePage(TemplateView):
    template_name = "homepage.html"


"""class PostListView(ListView):
    model = Post
    template_name = "listview.html"
    context_object_name = "posts"
    paginate_by = 10
    
    def get_queryset(self):"""





