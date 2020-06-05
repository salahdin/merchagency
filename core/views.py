from django.shortcuts import get_list_or_404
from django.views.generic import ListView,TemplateView
from .models import *


class HomePage(TemplateView):
    template_name = "homepage.html"


class PostListView(ListView):
    model = Post
    template_name = "listview.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def userfeed(request):
    """
    user feed
    :param request:
    :return:
    """
    pass


def post(request):
    """
    user posts adverts
    :param request:
    :return:
    """
    pass






