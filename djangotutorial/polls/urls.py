from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="indess"), # O 'name' é usado para referenciar essa URL em templates ou código Python.
]