from django.apps import AppConfig


class FlashcardsConfig(AppConfig):
    """
    Конфигурация приложения для работы с карточками.

    Этот класс настраивает параметры приложения "flashcards", включая
    использование поля автоматического увеличения BigAutoField в качестве
    стандартного поля для идентификаторов моделей.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flashcards'

