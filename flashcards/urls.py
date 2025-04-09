from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_card, name='add_card'),
    path('cards/', views.view_cards, name='view_cards'),
    path('quiz/', views.quiz, name='quiz'),
]
