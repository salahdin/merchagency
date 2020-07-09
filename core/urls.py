from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.HomePage.as_view(template_name="templates/landingpage.html")),
    path('post/', views.post, name="post"),
    path('feed/', views.userfeed, name="list_view"),
    path('search/', views.SearchResultsView.as_view(), name="search_results"),
    path('follow/<int:id_>', views.follow, name="follow"),
    path('registerservice/', views.register_service,name="register_service"),
    path('mypost/', views.mypost, name='mypost'),
    path('findnew/',views.findservices,name='findservices'),
]