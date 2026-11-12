from django.contrib import admin
from .models import Gra

@admin.register(Gra)
class GraAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'gatunek', 'rok_wydania', 'dostepna', 'wydawca', 'ocena')
    list_filter = ('dostepna', 'gatunek', 'wydawca')
    search_fields = ('tytul', 'wydawca')