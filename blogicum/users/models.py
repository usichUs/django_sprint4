from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    """
    Кастомная модель пользователя.
    """
    def get_absolute_url(self):
        """
        Возвращает URL для профиля пользователя.
        """
        return reverse('blog:profile', kwargs={'username': self.username})
