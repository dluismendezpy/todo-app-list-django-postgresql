# Django
from django.contrib import admin
from django.urls import path, include

# Owns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls'))
]
