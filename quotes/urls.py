from django.urls import path
from .views import home, RandomQuoteView

urlpatterns = [
    path('', home, name='home'),  # Halaman utama
    path('random/', RandomQuoteView.as_view(), name='random-quote'),  # API untuk kutipan acak
]
