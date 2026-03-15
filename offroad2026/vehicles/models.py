from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Vehicle(models.Model):
    brand = models.CharField(
        max_length=50,
    )

    model = models.CharField(
        max_length=50,
    )

    year = models.IntegerField(
        validators=[
            MinValueValidator(1980),
            MaxValueValidator(2026)
        ]
    )
    horsepower = models.PositiveIntegerField()

    description = models.TextField()

    image_url = models.URLField()

    class Meta:
        ordering = ["brand", "model"]

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"