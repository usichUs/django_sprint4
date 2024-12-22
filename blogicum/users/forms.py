from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """
    Кастомная форма для создания нового пользователя.

    Наследуется от UserCreationForm и добавляет дополнительные поля:
    - username
    - email
    - first_name
    - last_name
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class EditUserProfileForm(forms.ModelForm):
    """
    Форма для редактирования профиля пользователя.

    Включает поля:
    - username
    - email
    - first_name
    - last_name
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
