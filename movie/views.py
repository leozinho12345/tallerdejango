from django.shortcuts import render
from .models import Movie, News

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    return render(request, 'home.html', {
        'searchTerm': searchTerm,
        'movies': movies
    })

def about(request):
    return render(request, 'about.html')

def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss': newss})

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render
from .models import Movie, News

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    return render(request, 'home.html', {
        'searchTerm': searchTerm,
        'movies': movies
    })

def about(request):
    return render(request, 'about.html')

def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss': newss})

def statistics_view(request):
    # Agrupar películas por año
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('year')
    movie_counts_by_year = {}
    
    for year in years:
        if year:
            movies_in_year = Movie.objects.filter(year=year).count()
            movie_counts_by_year[year] = movies_in_year

    # Generar la gráfica
    bar_width = 0.5
    movie_positions = range(len(movie_counts_by_year))
    
    plt.figure(figsize=(10, 5))
    plt.bar(movie_positions, movie_counts_by_year.values(), width=bar_width, align='center', color='#0d6efd')
    plt.xticks(movie_positions, movie_counts_by_year.keys(), rotation=45)
    plt.xlabel('Año')
    plt.ylabel('Número de Películas')
    plt.title('Películas por Año')
    plt.tight_layout()

    # Convertir gráfica a base64 para HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()

    graphic = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'statistics.html', {'graphic': graphic})