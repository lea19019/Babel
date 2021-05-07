from django.urls import path
from . import views

urlpatterns = [
    path('', views.music_info, name='music_info'),
    path('song', views.SongCreateView.as_view(), name='song_register'),
]
