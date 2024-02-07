from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    #path("<str:first_name>", views.index, name="first_name"),
    path("submit-slayer/", views.submit_slayer, name="submit_slayer"),
    path("slayer-list/", views.slayer_list, name="slayer_list"),
    path("categories/humans/", views.human, name="humans"),
    path("categories/demons/", views.demon, name="demons"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog")
]