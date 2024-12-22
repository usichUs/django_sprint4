from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserCreationForm, EditUserProfileForm

User = get_user_model()


class UserCreateView(CreateView):
    """
    Представление для регистрации нового пользователя.

    Шаблон: 'registration/registration_form.html'
    Форма: CustomUserCreationForm
    После успешной регистрации пользователь автоматически авторизуется 
    и перенаправляется на главную страницу блога.
    """
    template_name = 'registration/registration_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """
        Сохраняет нового пользователя, выполняет вход и перенаправляет на главную.
        """
        user = form.save()
        login(self.request, user)
        return redirect('blog:index')


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Представление для редактирования профиля пользователя.

    Доступно только авторизованным пользователям.
    Шаблон: 'blog/user.html'
    Форма: EditUserProfileForm
    """
    model = User
    form_class = EditUserProfileForm
    template_name = 'blog/user.html'

    def get_object(self):
        """
        Возвращает текущего авторизованного пользователя.
        """
        return self.request.user
