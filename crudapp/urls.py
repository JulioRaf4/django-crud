from django.urls import path
from .views import *


urlpatterns = [
    path("", view=index, name='pessoa'),
    path("pessoa/", PessoaListView.as_view(), name='pessoa'),
    path('pessoa/create/', PessoaCreateView.as_view(), name='pessoa_create'),
    path('pessoa/update/<int:pk>', PessoaUpdateView.as_view(), name='pessoa_update'),
    path('pessoa/delete/<int:pk>', PessoaDeleteView.as_view(), name='pessoa_delete')
]
