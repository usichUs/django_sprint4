from django.shortcuts import render
from django.views.generic import TemplateView


class AboutTemplateView(TemplateView):
    """
    Представление для отображения страницы "О нас".
    """
    template_name = 'pages/about.html'


class RulesTemplateView(TemplateView):
    """
    Представление для отображения страницы с правилами.
    """
    template_name = 'pages/rules.html'


def permission_denied(request, exception):
    """
    Обработчик ошибки 403: доступ запрещён.

    Отображает кастомную страницу ошибки 403.
    """
    return render(request, 'pages/403.html', status=403)


def csrf_failure(request, reason=''):
    """
    Обработчик ошибки CSRF.

    Отображает кастомную страницу ошибки CSRF.
    """
    return render(request, 'pages/403csrf.html', status=403)


def page_not_found(request, exception):
    """
    Обработчик ошибки 404: страница не найдена.

    Отображает кастомную страницу ошибки 404.
    """
    return render(request, 'pages/404.html', status=404)


def server_error(request):
    """
    Обработчик ошибки 500: внутренняя ошибка сервера.

    Отображает кастомную страницу ошибки 500.
    """
    return render(request, 'pages/500.html', status=500)
