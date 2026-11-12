from django.shortcuts import render
from django.http import JsonResponse
from .models import Gra


def index(request):
    return render(request, 'Katalog/index.html')


def api_gry_list(request):
    gry_qs = Gra.objects.all().order_by('tytul')

    dostepna_param = request.GET.get('dostepna', None)
    if dostepna_param is not None:
        if dostepna_param.lower() in ['true', '1']:
            gry_qs = gry_qs.filter(dostepna=True)
        elif dostepna_param.lower() in ['false', '0']:
            gry_qs = gry_qs.filter(dostepna=False)

    gry_qs = gry_qs[:10]

    data = []
    for g in gry_qs:
        data.append({
            'id': g.id,
            'tytul': g.tytul,
            'gatunek': g.gatunek,
            'opis': g.opis,
            'rok_wydania': g.rok_wydania,
            'dostepna': g.dostepna,
            'wydawca': g.wydawca,
            'ocena': str(g.ocena) if g.ocena else None,
        })

    return JsonResponse({'items': data})