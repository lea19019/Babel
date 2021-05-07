from django.shortcuts import render, get_object_or_404
# We will get all of our music info with this line
from . import models
from django.views import generic

# Create your views here.


def music_info(request):
    songs = models.Music.objects.all()
    context = {'songs': songs}
    return render(request, 'music.html', context)


class SongCreateView(generic.CreateView):
    model = models.Music
    template_name = 'song_form.html'
    fields = ['name', 'artist', 'url']
