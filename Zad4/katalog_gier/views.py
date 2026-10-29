from django.shortcuts import render
from django.http import JsonResponse
from .models import Gra


def index(request):
    return render(request, 'katalog_gier/index.html')


def api_gry_list(request):
    # Odczyt parametru filtra z adresu URL
    dostepna_param = request.GET.get('dostepna', None)

    # Pobranie danych przez ORM
    gry_qs = Gra.objects.all()

    # Filtrowanie ORM po stronie serwera
    if dostepna_param is not None:
        if dostepna_param.lower() in ['true', '1']:
            gry_qs = gry_qs.filter(dostepna=True)
        elif dostepna_param.lower() in ['false', '0']:
            gry_qs = gry_qs.filter(dostepna=False)

    # Przygotowanie listy ze struktury JSON (zwraca min. 3 pola każdego rekordu)
    data = []
    for g in gry_qs:
        data.append({
            'id': g.id,
            'tytul': g.tytul,
            'gatunek': g.gatunek,
            'opis': g.opis,
            'rok_wydania': g.rok_wydania,
            'dostepna': g.dostepna,
        })

    return JsonResponse({'items': data})