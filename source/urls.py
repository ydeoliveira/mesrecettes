from django.urls import path
from source.viewsautocomplete import SourceAutocomplete

urlpatterns = [
        path('source-autocomplete/', SourceAutocomplete.as_view(), name='source-autocomplete')
]