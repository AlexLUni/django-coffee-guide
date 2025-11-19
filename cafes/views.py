from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    """
    Главная страница: поиск, фильтры, несколько карточек кафе.
    """
    example_cafes = [
        {
            "name": "Дрип & Дрифт",
            "tagline": "Спешиалти-кофейня рядом с парком",
            "area": "Центр",
            "features": "V60, фильтр, десерты",
        },
        {
            "name": "Сова и Зёрна",
            "tagline": "Поздно открыта, тихо и с розетками",
            "area": "Юг",
            "features": "Wi-Fi, розетки, посадка у окна",
        },
        {
            "name": "Эспрессо Бар №3",
            "tagline": "Забежать за шотом по пути",
            "area": "Север",
            "features": "Эспрессо, раф, to-go",
        },
    ]
    context = {
        "cafes": example_cafes,
    }
    return render(request, "cafes/home.html", context)


def cafe_list(request: HttpRequest) -> HttpResponse:
    """
    Страница со списком всех кофеен.
    """
    return render(request, "cafes/cafe_list.html")


def cafe_detail(request: HttpRequest, slug: str) -> HttpResponse:
    """
    Страница конкретной кофейни.
    """
    context = {"slug": slug}
    return render(request, "cafes/cafe_detail.html", context)


def about(request: HttpRequest) -> HttpResponse:
    """
    Страница «О проекте».
    """
    return render(request, "cafes/about.html")
