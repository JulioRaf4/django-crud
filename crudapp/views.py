from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Pessoa
# Create your views here.


def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "home.html", {'pessoas': pessoas})


def salvar(request):
    vname = request.POST.get("name")
    Pessoa.objects.create(name=vname)
    pessoas = Pessoa.objects.all()
    return render(request, "home.html", {'pessoas': pessoas})


def edit(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "edit.html", {'pessoa': pessoa})


def update(request, id):
    vname = request.POST.get("name")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.name = vname
    pessoa.save()
    return redirect(home)


def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)