from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from cafes.forms import ReviewForm
from cafes.models import Cafe, Favorite, Review


def home(request: HttpRequest) -> HttpResponse:
    """
    Главная страница: поиск и несколько карточек.
    """
    cafes = Cafe.objects.order_by("-rating", "name")[:6]
    context = {"cafes": cafes}
    return render(request, "cafes/home.html", context)


def cafe_list(request: HttpRequest) -> HttpResponse:
    """
    Страница со списком кофеен, а также результатом поиска.
    """
    cafes_qs = Cafe.objects.all()

    query = request.GET.get("q", "").strip()
    if query:
        cafes_qs = cafes_qs.filter(
            Q(name__icontains=query)
            | Q(tagline__icontains=query)
            | Q(address__icontains=query)
            | Q(features__icontains=query)
            | Q(area__icontains=query)
        )

    if request.GET.get("open_now") == "1":
        cafes_qs = cafes_qs.filter(is_open_now=True)

    if request.GET.get("min_rating") == "4":
        cafes_qs = cafes_qs.filter(rating__gte=4.0)

    if request.GET.get("wifi") == "1":
        cafes_qs = cafes_qs.filter(has_wifi=True)

    price = request.GET.get("price")
    if price in {"$", "$$", "$$$"}:
        cafes_qs = cafes_qs.filter(price_level=price)

    cafes = cafes_qs.order_by("-rating", "name")

    has_filters = bool(
        query
        or request.GET.get("open_now") == "1"
        or request.GET.get("min_rating") == "4"
        or request.GET.get("wifi") == "1"
        or price in {"$", "$$", "$$$"}
    )

    context = {
        "cafes": cafes,
        "query": query,
        "has_filters": has_filters,
    }
    return render(request, "cafes/cafe_list.html", context)


def cafe_detail(request: HttpRequest, slug: str) -> HttpResponse:
    """
    Страница конкретной кофейни с отзывами и избранным.
    """
    cafe = get_object_or_404(Cafe, slug=slug)
    reviews = cafe.reviews.select_related("user").all()

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(
            user=request.user,
            cafe=cafe,
        ).exists()

    if request.method == "POST":
        if not request.user.is_authenticated:
            login_url = reverse("login")
            return HttpResponseRedirect(f"{login_url}?next={request.path}")

        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(
                cafe=cafe,
                user=request.user,
                rating=form.cleaned_data["rating"],
                text=form.cleaned_data["text"],
            )
            return redirect("cafes:cafe_detail", slug=cafe.slug)
    else:
        form = ReviewForm()

    context = {
        "cafe": cafe,
        "reviews": reviews,
        "form": form,
        "is_favorite": is_favorite,
    }
    return render(request, "cafes/cafe_detail.html", context)


@login_required
def toggle_favorite(request: HttpRequest, slug: str) -> HttpResponse:
    """
    Переключение состояния «избранное» для кофейни.
    """
    cafe = get_object_or_404(Cafe, slug=slug)

    if request.method == "POST":
        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            cafe=cafe,
        )
        if not created:
            favorite.delete()

    return redirect("cafes:cafe_detail", slug=cafe.slug)


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    """
    Страница профиля с избранным и отзывами.
    """
    favorites = Favorite.objects.filter(user=request.user).select_related("cafe")
    reviews = Review.objects.filter(user=request.user).select_related("cafe")

    context = {
        "favorites": favorites,
        "reviews": reviews,
    }
    return render(request, "cafes/profile.html", context)


def signup(request: HttpRequest) -> HttpResponse:
    """
    Регистрация нового пользователя.
    """
    if request.user.is_authenticated:
        return redirect("cafes:profile")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("cafes:profile")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


def about(request: HttpRequest) -> HttpResponse:
    """
    Страница «О проекте».
    """
    return render(request, "cafes/about.html")


def debug_404_page(request: HttpRequest) -> HttpResponse:
    return render(request, "404.html", status=404)


def page_not_found(request: HttpRequest, exception) -> HttpResponse:
    """Кастомная страница 404."""
    return render(request, "404.html", status=404)
