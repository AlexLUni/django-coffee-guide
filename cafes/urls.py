from django.urls import path

from . import views

app_name = "cafes"

urlpatterns = [
    path("", views.home, name="home"),
    path("cafes/", views.cafe_list, name="cafe_list"),
    path("cafes/<slug:slug>/", views.cafe_detail, name="cafe_detail"),
    path(
        "cafes/<slug:slug>/favorite/",
        views.toggle_favorite,
        name="toggle_favorite",
    ),
    path("about/", views.about, name="about"),
    path("profile/", views.profile, name="profile"),
    path("signup/", views.signup, name="signup"),
    path("debug-404/", views.debug_404_page, name="debug_404"),
]
