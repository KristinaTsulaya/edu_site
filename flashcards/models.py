from django.db import models

class Flashcard(models.Model):
    is_learned = models.BooleanField(default=False)
    last_review = models.DateTimeField(auto_now=True)
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)

    def __str__(self):
        return self.word
