from django.db import models
from django.core.validators import MinLengthValidator
from offroad2026.destinations.models import Destination
from offroad2026.vehicles.models import Vehicle


class Story(models.Model):
    title = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(5)],
    )

    content = models.TextField(
        validators=[MinLengthValidator(20)]
    )

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="stories",
    )

    vehicles = models.ManyToManyField(
        Vehicle,
        related_name="stories",
        blank=True,
    )

    trip_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-trip_date"]

    def __str__(self):
        return self.title