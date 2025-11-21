from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from cafes.models import Cafe


def home(request: HttpRequest) -> HttpResponse:
  """
  Главная страница: поиск и базовые фильтры по кофейням.
  """
  cafes_qs = Cafe.objects.all()

  # --- Поиск по строке q ---
  query = request.GET.get("q", "").strip()
  if query:
      cafes_qs = cafes_qs.filter(
          Q(name__icontains=query)
          | Q(tagline__icontains=query)
          | Q(address__icontains=query)
          | Q(features__icontains=query)
          | Q(area__icontains=query)
      )

  # --- Фильтр "Открыто сейчас" ---
  if request.GET.get("open_now") == "1":
      cafes_qs = cafes_qs.filter(is_open_now=True)

  # --- Фильтр "Рейтинг 4+" ---
  if request.GET.get("rating_gte") == "4":
      cafes_qs = cafes_qs.filter(rating__gte=4.0)

  # --- Фильтр "Wi-Fi" ---
  if request.GET.get("wifi") == "1":
      cafes_qs = cafes_qs.filter(has_wifi=True)

  # --- Фильтр по уровню цен ---
  price_level = request.GET.get("price_level")
  if price_level in {"$", "$$", "$$$"}:
      cafes_qs = cafes_qs.filter(price_level=price_level)

  cafes = cafes_qs.order_by("-rating", "name")[:30]

  context = {
      "cafes": cafes,
      "query": query,
  }
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
