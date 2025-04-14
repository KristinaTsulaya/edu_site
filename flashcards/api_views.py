from datetime import date
import hashlib
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Flashcard
from .serializers import FlashcardSerializer

class FlashcardListCreateAPIView(generics.ListCreateAPIView):
    """
    Обрабатывает запросы для получения списка всех карточек или для создания новой карточки.

    Этот класс наследует от ListCreateAPIView и позволяет пользователю:
    - Получить список всех карточек через GET-запрос.
    - Создать новую карточку через POST-запрос.

    Атрибуты:
        queryset (QuerySet): Все объекты модели Flashcard.
        serializer_class (Serializer): Сериализатор для модели Flashcard (FlashcardSerializer).
    """
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer

class WordOfTheDayAPIView(APIView):
    """
    Возвращает слово дня в виде карточки.

    Этот класс обрабатывает GET-запросы для получения "слова дня". Для этого используется хэширование текущей даты,
    чтобы каждый день отображалось новое слово из базы данных.

    Метод:
        GET: Возвращает карточку с "словом дня". Если карточек нет в базе данных, возвращается сообщение об ошибке.
    """
    def get(self, request, format=None):
        cards = Flashcard.objects.all()
        if not cards:
            return Response({'detail': 'No flashcards available.'}, status=404)

        # Генерация уникального хэш-значения на основе текущей даты
        hash_value = int(hashlib.sha256(str(date.today()).encode()).hexdigest(), 16)
        word_of_day = cards[hash_value % len(cards)]
        
        # Сериализация и возврат карточки
        serializer = FlashcardSerializer(word_of_day)
        return Response(serializer.data)
