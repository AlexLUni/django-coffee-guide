from __future__ import annotations

from django.db import models


class Cafe(models.Model):
    """
    Кофейня в городе.
    """

    slug = models.SlugField(
        verbose_name="URL-ярлык",
        max_length=80,
        unique=True,
        help_text="Короткое имя в URL, латиница, дефисы. Например: drip-and-drift.",
    )
    name = models.CharField(
        verbose_name="Название кофейни",
        max_length=120,
    )
    tagline = models.CharField(
        verbose_name="Короткое описание",
        max_length=200,
        blank=True,
    )
    city = models.CharField(
        verbose_name="Город",
        max_length=80,
        default="Москва",
    )
    area = models.CharField(
        verbose_name="Район / часть города",
        max_length=80,
        blank=True,
        help_text="Например: Центр, Юг, Таганка.",
    )
    address = models.CharField(
        verbose_name="Адрес",
        max_length=200,
    )

    price_level = models.CharField(
        verbose_name="Уровень цен",
        max_length=3,
        choices=[
            ("$", "Бюджетно"),
            ("$$", "Средний чек"),
            ("$$$", "Дороже среднего"),
        ],
        default="$$",
    )

    has_wifi = models.BooleanField(
        verbose_name="Есть Wi-Fi",
        default=True,
    )
    has_food = models.BooleanField(
        verbose_name="Есть еда / десерты",
        default=True,
    )

    features = models.CharField(
        verbose_name="Особенности",
        max_length=200,
        blank=True,
        help_text="Например: фильтр, V60, десерты, много розеток.",
    )

    rating = models.DecimalField(
        verbose_name="Рейтинг",
        max_digits=2,   # максимум 9.9
        decimal_places=1,
        null=True,
        blank=True,
    )

    is_open_now = models.BooleanField(
        verbose_name="Открыто сейчас (заглушка)",
        default=True,
        help_text="Пока руками, потом можно будет считать по расписанию.",
    )

    created_at = models.DateTimeField(
        verbose_name="Создано",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Обновлено",
        auto_now=True,
    )

    class Meta:
        verbose_name = "Кофейня"
        verbose_name_plural = "Кофейни"
        ordering = ["-rating", "name"]

    def __str__(self) -> str:
        return self.name
