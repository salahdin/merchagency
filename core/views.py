from django.shortcuts import get_list_or_404,redirect,get_object_or_404
from django.views.generic import ListView,TemplateView
from .models import *
from .forms import PostForm, ServiceForm
from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from userprofile.models import UserFollowing
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class HomePage(TemplateView):
    template_name = "templates/landingpage.html"


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        service_object_list = Service.objects.filter(
            Q(Service_name__contains=query) | Q(description__contains=query)
        )
        context['services'] = service_object_list
        post_object_list = Post.objects.filter(
            Q(postText__icontains=query)
        )
        context['posts'] = post_object_list
        return context


class AlternateSearchResultsView(ListView):
    model = Post
    template_name = 'serviceList.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(postText__icontains=query)
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
        usersIfollow.add(user.following_user_id)
    follow_new_users = Service.objects.all()[:5]
    posts = Post.objects.all().filter(postby__in=usersIfollow)[0:25]

    return render(request, 'homepage.html', {'posts': posts, 'some_users': follow_new_users})

@login_required(login_url="/")
def post(request):
    """
    user posts adverts
    :param request:
    :return:
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            try:
                service_instance = Service.objects.get(id=request.user.seller.id)
                post.postby = service_instance
                post.price = request.POST['price']
                if request.FILES:
                    docs = request.FILES
                    post.postImage = docs['postImage']
                post.save()
                return redirect('/')
            except Exception:
                messages.warning(request, 'please register your service first')
                return redirect('core:register_service')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

@login_required(login_url="/")
def register_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service_form = form.save(commit=False)
            user_instance = User.objects.get(id=request.user.id)
            service_form.user = user_instance
            """docs = request.FILES
            service_form.avi = docs['avi']"""
            service_form.save()
            return redirect('/')
    else:
        form = ServiceForm()
    return render(request, 'registerService.html', {'form': form})


def follow(request, id_):
    if request.method == "GET":
        print("hello")
        userToFollow = get_object_or_404(Service, id=id_)
        try:
            UserFollowing.objects.create(
                user_id = request.user,
                following_user_id=userToFollow,
            )
        except Exception:
            print("dosent work")
            pass
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def mypost(request):
    try:
        service_instance = Service.objects.get(id=request.user.seller.id)
        post = service_instance.servicepost.all()
    except Exception:
        pass

    return render(request, 'myposts.html', {'posts': post})


def findservices(request):
    services = Service.objects.all().order_by('createDate')[:10]
    return render(request,'findservices.html',{'services':services})

