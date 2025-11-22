from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .cafe import Cafe


class Review(models.Model):
    """Отзыв."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cafe_reviews",
    )
    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
        verbose_name="Оценка",
    )
    text = models.TextField(
        verbose_name="Отзыв",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.cafe}: {self.rating}★ от {self.user}"
