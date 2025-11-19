from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    cafes = [
        {
            "name": "Brew & Chill",
            "tagline": "Спешелти-кофе и тихая музыка.",
            "city": "Москва",
            "address": "ул. Примерная, 10",
            "average_bill": 350,
            "format": "спешелти",
        },
        {
            "name": "City Coffee",
            "tagline": "Забегай по пути на работу.",
            "city": "Москва",
            "address": "пр-т Центральный, 5",
            "average_bill": 250,
            "format": "to go",
        },
        {
            "name": "Латте & Книги",
            "tagline": "Кофе и полки с любимыми книгами.",
            "city": "Москва",
            "address": "наб. Речная, 3",
            "average_bill": 400,
            "format": "кофейня + коворкинг",
        },
    ]

    context = {
        "cafes": cafes,
    }
    return render(request, "cafes/home.html", context)
