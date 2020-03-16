from django.shortcuts import render
from django.http import HttpResponse
from .models import MessageDB
from django.template import loader
from . import forms,models
from django.template.context_processors import csrf
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .forms import SignUpForm
from .forms import MessageForm

# Create your views here.

def index(request):
    return render(request,'index.html')


def home(request):
    form = MessageForm(request.POST or None)
    form1 = forms.MessageForm()
    message_db = MessageDB.objects.all()
    data = {
    'message' : form1,
    'message_db': message_db
    }
    if form.is_valid():
        models.MessageDB.objects.create(**form.cleaned_data)
        return redirect('home')

    return render(request,'home.html',data)



class SignUp(CreateView):
    form_class = SignUpForm

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
