from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("offroad2026.common.urls")),
    path("destinations/", include("offroad2026.destinations.urls")),
    path("vehicles/", include("offroad2026.vehicles.urls")),
    path("stories/", include("offroad2026.stories.urls")),
]