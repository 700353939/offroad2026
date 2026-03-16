from django.urls import path
from offroad2026.vehicles.views import (
    VehicleListView, VehicleDetailView, VehicleCreateView, VehicleEditView,
)

urlpatterns = [
    path("", VehicleListView.as_view(), name="vehicle-list"),

    path("create/", VehicleCreateView.as_view(), name="vehicle-create"),

    path("<int:pk>/", VehicleDetailView.as_view(), name="vehicle-details"),

    path("<int:pk>/edit/", VehicleEditView.as_view(), name="vehicle-edit"),
]