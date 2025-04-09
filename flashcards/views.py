from django.shortcuts import render, redirect
from .models import Flashcard
from .forms import FlashcardForm
import random

def index(request):
    return render(request, 'flashcards/index.html')

def view_cards(request):
    cards = Flashcard.objects.all()
    return render(request, 'flashcards/view_cards.html', {'cards': cards})

def add_card(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_cards')
    else:
        form = FlashcardForm()
    return render(request, 'flashcards/add_card.html', {'form': form})

def quiz(request):
    cards = list(Flashcard.objects.all())
    if not cards:
        return render(request, 'flashcards/quiz.html', {'message': 'Нет доступных карточек.'})

    card = random.choice(cards)
    result = None

    if request.method == 'POST':
        user_answer = request.POST.get('answer', '').strip().lower()
        correct = request.POST.get('correct', '').strip().lower()
        result = (user_answer == correct)

    return render(request, 'flashcards/quiz.html', {'card': card, 'result': result})
