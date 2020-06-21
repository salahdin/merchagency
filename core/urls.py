from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('home/', views.HomePage.as_view(template_name="core/templates/post.html")),
    path('post/', views.post, name="post"),
    path('feed/', views.userfeed, name="list_view"),
    path('search/', views.SearchResultsView.as_view(), name="search_results"),
]