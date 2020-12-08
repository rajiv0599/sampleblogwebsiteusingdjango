from django.contrib import admin
from django.urls import path,include
from . import views
from .views import postdetail,blogview

urlpatterns = [
    
    #path('',views.home,name='home'),
    #path('blogpage',views.bpage,name='bpage')
    path("",blogview.as_view(),name="home"),
    path("<int:pk>",postdetail.as_view(),name="blog-detail"),
    #path("post/<int:pk>",dem.as_view(),name="blog-detail")
    path("search",views.search,name="search"),
]