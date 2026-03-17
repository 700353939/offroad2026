from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from offroad2026.destinations.models import Destination
from offroad2026.destinations.forms import DestinationCreateForm, DestinationEditForm


class DestinationListView(ListView):
    model = Destination
    template_name = "destinations/destination-list.html"
    context_object_name = "destinations"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("q")
        sort = self.request.GET.get("sort")

        if search:
            queryset = queryset.filter(name__icontains=search)

        if sort == "name":
            queryset = queryset.order_by("name")
        elif sort == "difficulty":

            difficulty_order = {"easy": 0, "medium": 1, "hard": 2}
            queryset = sorted(
                queryset,
                key=lambda d: difficulty_order.get(d.difficulty, 99)
            )

        return queryset


class DestinationDetailView(DetailView):
    model = Destination
    template_name = "destinations/destination-details.html"
    context_object_name = "destination"


class DestinationCreateView(CreateView):
    model = Destination
    form_class = DestinationCreateForm
    template_name = "destinations/destination-create.html"
    success_url = reverse_lazy("destination-list")


class DestinationEditView(UpdateView):
    model = Destination
    form_class = DestinationEditForm
    template_name = "destinations/destination-edit.html"
    success_url = reverse_lazy("destination-list")


class DestinationDeleteView(DeleteView):
    model = Destination
    template_name = "destinations/destination-delete.html"
    success_url = reverse_lazy("destination-list")
