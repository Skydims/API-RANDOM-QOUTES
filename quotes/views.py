import random
from django.shortcuts import render  # Tambahkan ini
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Quote
from .serializers import QuoteSerializer

class RandomQuoteView(APIView):
    def get(self, request):
        quotes = Quote.objects.all()
        if not quotes.exists():
            return Response({"error": "No quotes available"}, status=404)
        random_quote = random.choice(quotes)
        serializer = QuoteSerializer(random_quote)
        return Response(serializer.data)

def home(request):
    return render(request, 'quotes/home.html')
