from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    #  path('favorites/', views.favorites_page, name='favorites_page'),
    path('about/', views.about, name='about'),
    path('search/', views.movie_search, name='movie_search'),
    path('movies/', views.movie_list, name='movie_list'),
    # path('movies/<int:movie_id>/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('movies/<int:movie_id>/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/', views.favorites_page, name='favorites_page'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/<str:movie_title>/', views.movie_detail_by_title, name='movie_detail_by_title'),
    # Other URL patterns...
]
