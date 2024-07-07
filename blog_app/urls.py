from django.urls import path
from . views import post_detail, post_list, category_detail, search, contact, about

urlpatterns = [
    path("detail/<int:pk>",post_detail, name="detail"),
    path("lists/",post_list, name="list"),
    path("category/<int:pk>",category_detail , name="category_detail"),
    path("search/",search , name="search"),
    path("contact/",contact , name="contact"),
    path("about/",about , name="about"),



]
