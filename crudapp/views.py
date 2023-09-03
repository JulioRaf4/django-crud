from django.urls import reverse_lazy
from .forms import PessoaForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Pessoa
from django.contrib import messages
from django.views.generic import ListView


## GENERIC VIEWS ##

def index(request):
    return render(request, 'base.html')


class PessoaListView(ListView):
    model = Pessoa
    template_name = 'pessoa/pessoa_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pessoas"] = self.model.objects.all()
        return context


class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'pessoa/pessoa_form.html'
    success_url = reverse_lazy('pessoa')


class PessoaUpdateView(UpdateView):
    model = Pessoa
    fields = "__all__"
    template_name = 'pessoa/pessoa_form.html'
    success_url = reverse_lazy("pessoa")

class PessoaDeleteView(DeleteView):
    model = Pessoa
    template_name = 'pessoa/pessoa_confirm_delete.html'
    success_url = reverse_lazy("pessoa")
