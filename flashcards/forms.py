from django import forms
from .models import Flashcard

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['word', 'translation']
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control'}),
            'translation': forms.TextInput(attrs={'class': 'form-control'}),
        }
