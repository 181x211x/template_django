from django.shortcuts import render
from django.http import HttpResponse
from .models import message
from django.template import loader
from . import forms
from django.contrib.auth import login, authenticate


# Create your views here.

def index(request):
    return render(request,'index.html')


def login(request):
    return render(request,'login.html')


def logout(request):
    return render(request,'logout.html')
