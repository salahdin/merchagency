from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.HomePage.as_view(template_name="core/templates/post.html")),
    path('post/', views.post),
    path('feed/', views.userfeed, name="list_view"),
    path('search/', views.SearchResultsView.as_view(), name="search_results"),
]