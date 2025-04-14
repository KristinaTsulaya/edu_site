from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date
import hashlib
from .models import Flashcard
from .serializers import FlashcardSerializer

class FlashcardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer

class WordOfTheDayAPIView(APIView):
    def get(self, request, format=None):
        cards = Flashcard.objects.all()
        if not cards:
            return Response({'detail': 'No flashcards available.'}, status=404)

        hash_value = int(hashlib.sha256(str(date.today()).encode()).hexdigest(), 16)
        word_of_day = cards[hash_value % len(cards)]
        serializer = FlashcardSerializer(word_of_day)
        return Response(serializer.data)