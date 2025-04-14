import re
from django import forms
from .models import Flashcard

class FlashcardForm(forms.ModelForm):
    """
    Форма для создания и редактирования карточек с словом и переводом.

    Эта форма использует модель Flashcard и проверяет следующие поля:
    - 'word': должно содержать только латинские символы и пробелы.
    - 'translation': должно содержать только символы кириллицы и пробелы.
    """
    class Meta:
        model = Flashcard
        fields = ['word', 'translation']
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control'}),
            'translation': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_word(self):
        """
        Проверка поля 'word', чтобы оно содержало только латинские символы и пробелы.
        """
        word = self.cleaned_data['word']
        if not re.match(r'^[a-zA-Z\s]+$', word):
            raise forms.ValidationError("Поле должно содержать только латинские символы и пробелы.")
        return word

    def clean_translation(self):
        """
        Проверка поля 'translation', чтобы оно содержало только символы кириллицы и пробелы.
        """
        translation = self.cleaned_data['translation']
        if not re.match(r'^[а-яА-Я\s]+$', translation):
            raise forms.ValidationError("Поле должно содержать только символы кириллицы и пробелы.")
        return translation
