from django.core.management.base import BaseCommand
from ksiazki.models import Ksiazka

class Command(BaseCommand):

    def handle(self, *args, **options):
        ksiazki = [
            {'tytul': 'Lalka', 'autor': 'Bolesław Prus', 'rok_wydania': 1890},
            {'tytul': 'Pan Tadeusz', 'autor': 'Adam Mickiewicz', 'rok_wydania': 1834},
            {'tytul': 'Quo Vadis', 'autor': 'Henryk Sienkiewicz', 'rok_wydania': 1896},
            {'tytul': 'Ferdydurke', 'autor': 'Witold Gombrowicz', 'rok_wydania': 1937},
            {'tytul': 'Zbrodnia i kara', 'autor': 'Fiodor Dostojewski', 'rok_wydania': 1866},  # rosyjska, ale często czytana w Polsce
            {'tytul': 'Noce i dnie', 'autor': 'Maria Dąbrowska', 'rok_wydania': 1932},
            {'tytul': 'Chłopi', 'autor': 'Władysław Reymont', 'rok_wydania': 1904},
            {'tytul': 'Granica', 'autor': 'Zofia Nałkowska', 'rok_wydania': 1935},
            {'tytul': 'Solaris', 'autor': 'Stanisław Lem', 'rok_wydania': 1961},
            {'tytul': 'Pamiętnik z powstania warszawskiego', 'autor': 'Miron Białoszewski', 'rok_wydania': 1970},
            {'tytul': 'Medaliony', 'autor': 'Zofia Nałkowska', 'rok_wydania': 1946},
            {'tytul': 'Potop', 'autor': 'Henryk Sienkiewicz', 'rok_wydania': 1886},
            {'tytul': 'Krzyżacy', 'autor': 'Henryk Sienkiewicz', 'rok_wydania': 1900},
            {'tytul': 'Wesele', 'autor': 'Stanisław Wyspiański', 'rok_wydania': 1901},
            {'tytul': 'Ziemia obiecana', 'autor': 'Władysław Reymont', 'rok_wydania': 1899},
            {'tytul': 'Dziady', 'autor': 'Adam Mickiewicz', 'rok_wydania': 1823},
            {'tytul': 'Inny świat', 'autor': 'Gustaw Herling-Grudziński', 'rok_wydania': 1951},
            {'tytul': 'Faraon', 'autor': 'Bolesław Prus', 'rok_wydania': 1897},
            {'tytul': 'Balladyna', 'autor': 'Juliusz Słowacki', 'rok_wydania': 1834},
            {'tytul': 'Kamienie na szaniec', 'autor': 'Aleksander Kamiński', 'rok_wydania': 1943},
        ]

        for ksiazka in ksiazki:
            Ksiazka.objects.create(**ksiazka)
            self.stdout.write(f'Dodano: {ksiazka["tytul"]} - {ksiazka["autor"]}')

        self.stdout.write(self.style.SUCCESS('Dodano wszystkie 20 książek!'))
