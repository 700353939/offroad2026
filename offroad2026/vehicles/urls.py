from django.urls import path
from offroad2026.vehicles.views import (
    VehicleListView, VehicleDetailView, VehicleCreateView, VehicleEditView, VehicleDeleteView,
)

urlpatterns = [
    path("", VehicleListView.as_view(), name="vehicle-list"),

    path("create/", VehicleCreateView.as_view(), name="vehicle-create"),

    path("<int:pk>/", VehicleDetailView.as_view(), name="vehicle-details"),

    path("<int:pk>/edit/", VehicleEditView.as_view(), name="vehicle-edit"),

    path("<int:pk>/delete/", VehicleDeleteView.as_view(), name="vehicle-delete"),
]