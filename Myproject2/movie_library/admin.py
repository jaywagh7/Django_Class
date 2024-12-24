from django.contrib import admin
from .models import Director, Producer, Movie, Viewer, Viewing, MovieViewer

# Register models using the @admin.register decorator

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'director', 'producer')

@admin.register(Viewer)
class ViewerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(Viewing)
class ViewingAdmin(admin.ModelAdmin):
    list_display = ('viewer', 'movie', 'date_started', 'date_finished')

@admin.register(MovieViewer)
class MovieViewerAdmin(admin.ModelAdmin):
    list_display = ('title',)
