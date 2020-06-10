from django.shortcuts import get_list_or_404,redirect
from django.views.generic import ListView,TemplateView
from .models import *
from .forms import PostForm
from django.shortcuts import render


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

    usersIfollow = []
    for id in request.user.following.all():
        usersIfollow.append(id.user)

    usersIfollow.append(request.user.id)
    posts = Post.objects.filter(user_id__in=usersIfollow)[0:25]

    return render(request, 'homepage.html', {'posts': posts})


def post(request):
    """
    user posts adverts
    :param request:
    :return:
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.postby = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'homepage.html', {'form': form})








