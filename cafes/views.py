from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Cafe


def home(request: HttpRequest) -> HttpResponse:
  """
  Главная страница: показываем несколько кофеен “поблизости”.
  """
  cafes = (
      Cafe.objects
      .filter(is_open_now=True)
      .order_by("-rating", "name")[:6]
  )
  context = {"cafes": cafes}
  return render(request, "cafes/home.html", context)


def cafe_list(request: HttpRequest) -> HttpResponse:
    """
    Страница со списком всех кофеен.
    """
    cafes = Cafe.objects.order_by("-rating", "name")
    context = {"cafes": cafes}
    return render(request, "cafes/cafe_list.html", context)


def cafe_detail(request: HttpRequest, slug: str) -> HttpResponse:
  """
  Страница конкретной кофейни.
  """
  cafe = get_object_or_404(Cafe, slug=slug)
  context = {"cafe": cafe}
  return render(request, "cafes/cafe_detail.html", context)


def about(request: HttpRequest) -> HttpResponse:

    """
    Страница «О проекте».
    """
    return render(request, "cafes/about.html")
