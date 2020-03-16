from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import MessageDB
from datetime import datetime

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='必須 有効なメールアドレスを入力してください。',
        label='Eメールアドレス'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class MessageForm(forms.Form):
    username = forms.CharField(label='名前',max_length=20)
    message = forms.CharField(label='本文',max_length=200)
    date = forms.DateField(label='作成日',initial=datetime.now())
