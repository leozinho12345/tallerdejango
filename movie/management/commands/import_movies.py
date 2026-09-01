import csv
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = 'Carga películas desde movies_initial.csv'

    def handle(self, *args, **kwargs):
        with open('movies_initial.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Movie.objects.get_or_create(
                    title=row['title'],
                    description=row['description'],
                    genre=row['genre'],
                    year=int(row['year']),
                    image=row['image']
                )
        self.stdout.write(self.style.SUCCESS('Peliculas cargadas'))