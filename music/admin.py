from django.contrib import admin
# This will import the data from our Music app
from .models import Music

# Register your models here.
admin.site.register(Music)