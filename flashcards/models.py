from django.db import models

class Flashcard(models.Model):
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)

    def __str__(self):
        return self.word
