from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "account_id",
            "email",
            "first_name",
            "last_name",
        )

class LoginForm(AuthenticationForm): # ログインフォームを追加
    class Meta:
        model = User