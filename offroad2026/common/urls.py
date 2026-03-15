from django.urls import path
from offroad2026.common.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]