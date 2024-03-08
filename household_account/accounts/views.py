from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import SignUpForm, LoginForm # サインアップ、ログインフォーム


class IndexView(TemplateView): # """ ホームビュー """
    template_name = "index.html"

class SignupView(CreateView): # """ ユーザー登録用ビュー """
    form_class = SignUpForm   # 作成した登録用フォームを設定
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:index") # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form): # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=account_id, password=password)
        login(self.request, user)
        messages.success(self.request, '新規ユーザーを登録しました。')
        return response


class LoginView(BaseLoginView): # ログイン
    form_class = LoginForm
    template_name = "accounts/login.html"

class LogoutView(BaseLogoutView): # ログアウト
    success_url = reverse_lazy("accounts:index")