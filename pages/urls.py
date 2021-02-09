from django.urls import path

from . import views  # from all import views

app_name = "pages"  # name space
urlpatterns = [
    path("", views.index, name="index"),
]
