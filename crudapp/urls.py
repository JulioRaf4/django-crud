from django.urls import path
from .views import home, salvar, edit, update, delete

urlpatterns = [
    path("", home),
    path("salvar/", salvar, name="salvar"),
    path("edit/<int:id>", edit, name="edit"),
    path("update/<int:id>", update, name="update"),
    path("delete/<int:id>", delete, name="delete"),
]
