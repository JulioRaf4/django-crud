from django.urls import path
from .views import home, salvar, edit, update, delete, classe

urlpatterns = [
    path("", home),
    path("classe/", classe, name="classe"),
    path("salvar/", salvar, name="salvar"),
    path("edit/<int:id>", edit, name="edit"),
    path("update/<int:id>", update, name="update"),
    path("delete/<int:id>", delete, name="delete"),
]
