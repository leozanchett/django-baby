from django.urls import path

from . import views

app_name = "polls"  # Define o namespace para as URLs do aplicativo 'polls'. Isso é útil para evitar conflitos de nomes entre diferentes aplicativos.
# O 'app_name' é usado para referenciar as URLs em templates ou código Python,

urlpatterns = [
    path("", views.IndexView.as_view(), name="indess"), # O 'name' é usado para referenciar essa URL em templates ou código Python.
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detalhes"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:pk>/vote/", views.vote, name="vote"),
]