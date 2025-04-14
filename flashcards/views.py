from django.shortcuts import render, redirect, get_object_or_404
from .models import Flashcard
from .forms import FlashcardForm
from django.http import HttpResponse
import random

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

def delete_card(request, card_id):
    card = get_object_or_404(Flashcard, id=card_id)
    if request.method == 'POST':
        card.delete()
    return redirect('view_cards')

def index(request):
    total_cards = Flashcard.objects.count()
    context = {
        'total_cards': total_cards,
    }
    return render(request, 'flashcards/index.html', context)

def populate_flashcards(request):
    cards = [
        ("apple", "яблоко"),
        ("dog", "собака"),
        ("sun", "солнце"),
        ("moon", "луна"),
        ("house", "дом"),
        ("car", "машина"),
        ("tree", "дерево"),
        ("water", "вода"),
        ("book", "книга"),
        ("phone", "телефон"),
        ("chair", "стул"),
        ("table", "стол"),
        ("door", "дверь"),
        ("window", "окно"),
        ("pen", "ручка"),
        ("pencil", "карандаш"),
        ("school", "школа"),
        ("student", "студент"),
        ("teacher", "учитель"),
        ("computer", "компьютер"),
    ]

    created = 0
    for word, translation in cards:
        if not Flashcard.objects.filter(word=word, translation=translation).exists():
            Flashcard.objects.create(word=word, translation=translation)
            created += 1

    return HttpResponse(f"{created} карточек добавлено!")
