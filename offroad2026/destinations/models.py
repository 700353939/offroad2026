from django.db import models
from django.core.validators import MinLengthValidator

class Destination(models.Model):
    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
    )

    location = models.CharField(
        max_length=100,
    )

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
    )

    description = models.TextField()

    image_url = models.URLField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.location})"