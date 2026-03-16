from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from offroad2026.vehicles.models import Vehicle
from offroad2026.vehicles.forms import VehicleCreateForm, VehicleEditForm


class VehicleListView(ListView):
    model = Vehicle
    template_name = "vehicles/vehicle-list.html"
    context_object_name = "vehicles"


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = "vehicles/vehicle-details.html"
    context_object_name = "vehicle"


class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleCreateForm
    template_name = "vehicles/vehicle-create.html"
    success_url = reverse_lazy("vehicle-list")


class VehicleEditView(UpdateView):
    model = Vehicle
    form_class = VehicleEditForm
    template_name = "vehicles/vehicle-edit.html"
    success_url = reverse_lazy("vehicle-list")

class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = "vehicles/vehicle-delete.html"
    success_url = reverse_lazy("vehicle-list")