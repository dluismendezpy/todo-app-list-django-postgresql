# Django
from django.contrib import admin
from django.urls import path

# Owns

urlpatterns = [
    path('admin/', admin.site.urls),
]
