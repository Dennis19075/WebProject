from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.contacto, name="contacto"),
]
