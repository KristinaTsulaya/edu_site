from django.urls import path
from .api_views import FlashcardListCreateAPIView, WordOfTheDayAPIView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_card, name='add_card'),
    path('cards/', views.view_cards, name='view_cards'),
    path('quiz/', views.quiz, name='quiz'),
    path('delete/<int:card_id>/', views.delete_card, name='delete_card'),
    path('populate/', views.populate_flashcards, name='populate_flashcards'),
    path('check-word/', views.check_word, name='check_word'),

    path('api/flashcards/', FlashcardListCreateAPIView.as_view(), name='api_flashcards'),
    path('api/word-of-the-day/', WordOfTheDayAPIView.as_view(), name='word_of_the_day'),
]
