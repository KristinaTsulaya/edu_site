from django.db import models

class Flashcard(models.Model):
    """
    Модель для карточки, которая содержит слово и его перевод.

    Атрибуты:
    - 'word': слово на языке оригинала (максимальная длина 100 символов).
    - 'translation': перевод этого слова (максимальная длина 100 символов).
    """
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)

    def __str__(self):
        """
        Возвращает строковое представление объекта карточки (слово на языке оригинала).
        """
        return self.word
