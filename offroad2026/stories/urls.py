from django.urls import path
from offroad2026.stories.views import (
    StoryListView, StoryDetailView,StoryCreateView, StoryDeleteView, StoryEditView
)

urlpatterns = [
    path("", StoryListView.as_view(), name="story-list"),

    path("create/", StoryCreateView.as_view(), name="story-create"),

    path("<int:pk>/", StoryDetailView.as_view(), name="story-details"),

    path("<int:pk>/edit/", StoryEditView.as_view(), name="story-edit"),

    path("<int:pk>/delete/", StoryDeleteView.as_view(), name="story-delete"),
]