from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "last_name",
            "first_name",
        )

class LoginForm(AuthenticationForm): # ログインフォームを追加
    class Meta:
        model = CustomUser