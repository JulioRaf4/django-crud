from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
# Create your views here.


def login(request):
    return render(request, "crudproject/login.html")
