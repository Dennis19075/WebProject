from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.blog, name="blog"),
    path("categoria/<int:categoria_id>", views.categoria, name="categoria"),
]