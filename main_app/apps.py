from django.apps import AppConfig


class MainAppConfig(AppConfig):
    name = 'main_app'  # Указываем исходное имя приложения
    verbose_name = "Главные страницы"  # Имя которое необходимо отобразить в админке

