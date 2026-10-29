from django.shortcuts import render
from django.http import JsonResponse
from .models import Gra


def index(request):
    return render(request, 'katalog_gier/index.html')


def api_gry_list(request):
    dostepna_param = request.GET.get('dostepna', None)

    gry_qs = Gra.objects.all()

    if dostepna_param is not None:
        if dostepna_param.lower() in ['true', '1']:
            gry_qs = gry_qs.filter(dostepna=True)
        elif dostepna_param.lower() in ['false', '0']:
            gry_qs = gry_qs.filter(dostepna=False)

    data = []
    for g in gry_qs:
        data.append({
            'id': g.id,
            'tytul': g.tytul,
            'gatunek': g.gatunek,
            'opis': g.opis,
            'rok_wydania': g.rok_wydania,
            'dostepna': g.dostepna,
            'cena' : str(g.cena)
        })

    return JsonResponse({'items': data})