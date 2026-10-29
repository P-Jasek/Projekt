from django.db import models


class Gra(models.Model):
    tytul = models.CharField(max_length=100, verbose_name="Tytuł gry")
    gatunek = models.CharField(max_length=50, verbose_name="Gatunek")
    opis = models.TextField(verbose_name="Opis gry")
    rok_wydania = models.IntegerField(verbose_name="Rok wydania")
    dostepna = models.BooleanField(default=True, verbose_name="Dostępna w sklepie")
    cena = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, verbose_name="Cena (PLN)")

    class Meta:
        verbose_name = "Gra"
        verbose_name_plural = "Gry"
        
    def __str__(self):
        return f"{self.tytul} ({self.rok_wydania})"