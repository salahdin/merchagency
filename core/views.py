from django.shortcuts import get_list_or_404,redirect,get_object_or_404
from django.views.generic import ListView,TemplateView
from .models import *
from .forms import PostForm, ServiceForm
from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from userprofile.models import UserFollowing
from django.contrib.auth.decorators import login_required


class HomePage(TemplateView):
    template_name = "core/templates/landingpage.html"


class PostListView(ListView):
    model = Post
    template_name = "homepage.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class SearchResultsView(ListView):
    model = Service
    template_name = 'serviceList.html'
    context_object_name = 'services'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Service.objects.filter(
            Q(Service_name__contains=query) | Q(description__contains=query)
        )
        print(object_list)
        return object_list


@login_required(login_url="/")
def userfeed(request):
    """
    user feed
    :param request:
    :return:
    """

    usersIfollow = set()
    for user in request.user.follower.all():
        usersIfollow.add(user.id)

    posts = Post.objects.all().filter(postby__in=usersIfollow)[0:25]
    return render(request, 'homepage.html', {'posts': posts})

@login_required(login_url="/")
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
            service_instance = Service.objects.get(id=request.user.seller.id)
            post.postby = service_instance
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

@login_required(login_url="/")
def register_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service_form = form.save(commit=False)
            user_instance = User.objects.get(id=request.user.id)
            service_form = user_instance
            service_form.save()
            return redirect('/')
    else:
        form = ServiceForm()
    return render(request, 'post.html', {'form': form})


def follow(request, id_):
    if request.method == "GET":
        userToFollow = get_object_or_404(User, id=id_)
        try:
            UserFollowing.objects.create(
                user_id = request.user,
                following_user_id=userToFollow,
            )
        except Exception:
            pass
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


