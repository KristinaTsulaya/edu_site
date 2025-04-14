from rest_framework import serializers
from .models import Flashcard

class FlashcardSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Flashcard.

    Этот сериализатор преобразует объект модели Flashcard в формат, 
    который можно передать через API, и наоборот.

    Атрибуты:
    - 'word': строка, представляющая слово на языке оригинала.
    - 'translation': строка, представляющая перевод этого слова.
    """
    class Meta:
        model = Flashcard
        fields = '__all__'
