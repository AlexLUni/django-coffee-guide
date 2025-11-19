from django.urls import path

from . import views

app_name = "cafes"  # namespace для url'ов

urlpatterns = [
    path("", views.home, name="home"),
    path("cafes/", views.cafe_list, name="cafe_list"),
    path("cafes/<slug:slug>/", views.cafe_detail, name="cafe_detail"),
    path("about/", views.about, name="about"),
]
