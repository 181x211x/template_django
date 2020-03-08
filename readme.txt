**はじめに
これはDjangoのテンプレート用掲示板アプリケーションです

**準備
- python -m django --version //バージョン
- django-admin startproject プロジェクト名 //プロジェクト作成
- python manage.py runserver //サーバ起動
- python manage.py startapp アプリ名 //アプリ作成
- python manage.py migrate //DBテーブル作成
- python manage.py makemigrations polls //モデルに変更があったことを伝える
- python manage.py createsuperuser //管理者登録
-

◯ログイン認証のやり方
- ファイル構造
-- templatesの中にregistrationフォルダを作成
-- そこにlogin.htmlを作成
-- logout.htmlとsignup.htmlをtemplatesの中に作成

- setting
-- LOGIN_REDIRECT_URL = 'home'
-- LOGOUT_REDIRECT_URL = 'index'
-- ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'

- mysite/urls
- path('accounts/', include('django.contrib.auth.urls')),

- urls
-- path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
-- path('logout/', auth_views.LogoutView.as_view(), name='logout'),
-- path('signup/', SignUp.as_view(template_name='signup.html'), name='signup'),

- views
-- from django.contrib.auth import login, authenticate
-- from django.contrib.auth.forms import UserCreationForm
-- from django.views.generic.edit import CreateView
-- from django.shortcuts import redirect
-- class SignUp(CreateView):
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
-- ※viewにlogin logoutを作らない

- forms
-- from django.contrib.auth.forms import UserCreationForm
-- class SignUpForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
