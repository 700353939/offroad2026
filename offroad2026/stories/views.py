from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from offroad2026.stories.models import Story
from offroad2026.stories.forms import StoryCreateForm, StoryEditForm


class StoryListView(ListView):
    model = Story
    template_name = "stories/story-list.html"
    context_object_name = "stories"


class StoryDetailView(DetailView):
    model = Story
    template_name = "stories/story-details.html"
    context_object_name = "story"


class StoryCreateView(CreateView):
    model = Story
    form_class = StoryCreateForm
    template_name = "stories/story-create.html"
    success_url = reverse_lazy("story-list")


class StoryEditView(UpdateView):
    model = Story
    form_class = StoryEditForm
    template_name = "stories/story-edit.html"
    success_url = reverse_lazy("story-list")


class StoryDeleteView(DeleteView):
    model = Story
    template_name = "stories/story-delete.html"
    success_url = reverse_lazy("story-list")
