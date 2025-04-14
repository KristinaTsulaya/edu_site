import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Flashcard
from .forms import FlashcardForm

def view_cards(request):
    """
    Отображает список всех карточек.

    Эта функция получает все карточки из базы данных и передает их в шаблон
    для отображения на странице.
    """
    cards = Flashcard.objects.all()
    return render(request, 'flashcards/view_cards.html', {'cards': cards})

def add_card(request):
    """
    Добавляет новую карточку через форму.

    Эта функция обрабатывает запросы POST для добавления новой карточки. Если форма
    действительна, карточка сохраняется в базе данных, и пользователь перенаправляется на страницу
    со списком карточек.
    """
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_cards')
    else:
        form = FlashcardForm()
    return render(request, 'flashcards/add_card.html', {'form': form})

def quiz(request):
    """
    Проводит мини-викторину с случайной карточкой.

    Эта функция выбирает случайную карточку из базы данных и проверяет правильность ответа пользователя
    на вопрос о переводе этого слова. Результат проверки отображается на странице.
    """
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
    """
    Удаляет карточку по ID.

    Эта функция удаляет карточку из базы данных по заданному ID, если запрос был выполнен методом POST.
    После удаления пользователя перенаправляют на страницу со списком карточек.
    """
    card = get_object_or_404(Flashcard, id=card_id)
    if request.method == 'POST':
        card.delete()
    return redirect('view_cards')

def index(request):
    """
    Отображает главную страницу с количеством карточек.

    Эта функция отображает главную страницу приложения с информацией о
    количестве карточек в базе данных.
    """
    total_cards = Flashcard.objects.count()
    context = {
        'total_cards': total_cards,
    }
    return render(request, 'flashcards/index.html', context)

def check_word(request):
    """
    Проверяет наличие слова в базе (AJAX-запрос).

    Эта функция принимает слово через GET-параметр, проверяет его наличие в базе данных и
    возвращает ответ в формате JSON, сообщая, существует ли такое слово в базе.
    """
    word = request.GET.get('word', '').strip().lower()
    word_exists = Flashcard.objects.filter(word=word).exists()
    
    return JsonResponse({'exists': word_exists})

def populate_flashcards(request):
    """
    Автоматически заполняет базу наборами слов.

    Эта функция добавляет в базу данных несколько заранее заданных карточек с
    английскими словами и их переводами. Если карточка с таким словом уже существует,
    она не будет добавлена повторно. После завершения процесса пользователю отображается
    количество добавленных карточек.
    """
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
