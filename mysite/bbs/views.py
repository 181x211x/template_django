from django.shortcuts import render
from django.http import HttpResponse
from .models import message
from django.template import loader
from . import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import redirect


# Create your views here.

def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')


class SignUp(CreateView):
    form_class = UserCreationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/bbs_django/home/')
        return render(request, 'signup.html', {'form': form})
