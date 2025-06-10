from django.db import models

class Ksiazka(models.Model):
    tytul = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    rok_wydania = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tytul} ({self.rok_wydania})"
