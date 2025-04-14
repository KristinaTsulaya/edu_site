from django.urls import path
from .api_views import FlashcardListCreateAPIView, WordOfTheDayAPIView
from . import views

urlpatterns = [
    # Главная страница приложения
    path('', views.index, name='index'),

    # Страница для добавления новой карточки
    path('add/', views.add_card, name='add_card'),

    # Страница для просмотра всех карточек
    path('cards/', views.view_cards, name='view_cards'),

    # Страница с квизом для тестирования знаний
    path('quiz/', views.quiz, name='quiz'),

    # Маршрут для удаления карточки по ID
    path('delete/<int:card_id>/', views.delete_card, name='delete_card'),

    # Страница для массового добавления карточек
    path('populate/', views.populate_flashcards, name='populate_flashcards'),

    # Маршрут для проверки введенного слова
    path('check-word/', views.check_word, name='check_word'),

    # API маршрут для получения и создания карточек
    path('api/flashcards/', FlashcardListCreateAPIView.as_view(), name='api_flashcards'),

    # API маршрут для получения карточки слова дня
    path('api/word-of-the-day/', WordOfTheDayAPIView.as_view(), name='word_of_the_day'),
]
