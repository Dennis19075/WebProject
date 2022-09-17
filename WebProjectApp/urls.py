from django.urls import include, path

from WebProjectApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home", views.home, name="home"),
    path("store", views.store, name="store"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)