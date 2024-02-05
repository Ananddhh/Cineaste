from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import FavoriteMovie, Movie, Genre
from urllib.parse import unquote
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success_page.html')
        else:
            return render(request, 'error.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




@login_required
def add_to_favorites(request, movie_id):
    FavoriteMovie.objects.create(user=request.user, movie_id=movie_id)
    return redirect('favorites_page')

@login_required
def favorites_page(request):
    favorite_movies = FavoriteMovie.objects.filter(user=request.user)
    unique_movie_titles = set([movie.movie.title for movie in favorite_movies])
    return render(request, 'favorites_page.html', {'unique_movie_titles': unique_movie_titles})

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')


@login_required
def movie_list(request):
    movies = Movie.objects.all()
    favorite_movies = FavoriteMovie.objects.filter(user=request.user, movie__in=movies)
    favorited_movie_ids = [fav.movie_id for fav in favorite_movies]

    for movie in movies:
        if movie.id in favorited_movie_ids:
            movie.is_favorite = True
        else:
            movie.is_favorite = False

    return render(request, 'movie_list.html', {'movies': movies})


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})


@login_required
def movie_search(request):
    query = request.GET.get('query')  
    search_results = None
    
    if query:
        search_results = Movie.objects.filter(title__icontains=query)

    return render(request, 'search_results.html', {'search_results': search_results, 'query': query})



def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    is_favorite = False 

    return render(request, 'movie_detail.html', {'movie': movie, 'is_favorite': is_favorite})



def movie_detail_by_title(request, movie_title):
    decoded_title = unquote(movie_title)
    movie = get_object_or_404(Movie, title=decoded_title)
   
    return render(request, 'movie_detail.html', {'movie': movie})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'success_page2.html')  
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
