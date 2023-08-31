from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("salvar/", salvar, name="salvar"),
    path("edit/<int:id>", edit, name="edit"),
    path("update/<int:id>", update, name="update"),
    path("delete/<int:id>", delete, name="delete"),
]

urlpatterns += [
    path("pessoa/", PessoaListView.as_view()),
    path('pessoa/create/', PessoaCreateView.as_view(), name='pessoa_create'),
    path('pessoa/update/', PessoaUpdateView.as_view(), name='pessoa_update'),
]
