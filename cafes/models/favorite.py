from django.conf import settings
from django.db import models

from .cafe import Cafe


class Favorite(models.Model):
    """Избранное."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorite_cafes",
    )
    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"
        unique_together = ("user", "cafe")

    def __str__(self) -> str:
        return f"{self.user} → {self.cafe}"
