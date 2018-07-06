from django.apps import AppConfig


class MainAppConfig(AppConfig):
    name = 'main_app' # Здесь указываем исходное имя приложения
    verbose_name = "Главные страницы"  # А здесь, имя которое необходимо отобразить в админке

