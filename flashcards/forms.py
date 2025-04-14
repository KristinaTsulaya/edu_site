from django import forms
from .models import Flashcard
import re

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['word', 'translation']
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control'}),
            'translation': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_word(self):
        word = self.cleaned_data['word']
        if not re.match(r'^[а-яА-Я\s]+$', word):
            raise forms.ValidationError("Поле должно содержать только символы кириллицы и пробелы.")
        return word

    def clean_translation(self):
        translation = self.cleaned_data['translation']
        if not re.match(r'^[a-zA-Z\s]+$', translation):
            raise forms.ValidationError("Поле должно содержать только латинские символы и пробелы.")
        return translation