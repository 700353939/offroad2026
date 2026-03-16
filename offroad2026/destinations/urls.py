from django.urls import path
from offroad2026.destinations.views import (
    DestinationListView, DestinationDetailView, DestinationCreateView, DestinationEditView, DestinationDeleteView,
)

urlpatterns = [
    path("", DestinationListView.as_view(), name="destination-list"),

    path("create/", DestinationCreateView.as_view(), name="destination-create"),

    path("<int:pk>/", DestinationDetailView.as_view(), name="destination-details"),

    path("<int:pk>/edit/", DestinationEditView.as_view(), name="destination-edit"),

    path("<int:pk>/delete/", DestinationDeleteView.as_view(), name="destination-delete"),
]