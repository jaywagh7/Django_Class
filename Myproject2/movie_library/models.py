from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Producer(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    producer = models.OneToOneField(Producer, on_delete=models.SET_NULL, null=True, blank=True)
    viewers = models.ManyToManyField('Viewer', through='Viewing', related_name='movies')

    def __str__(self):
        return self.title

class Viewer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Viewing(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date_started = models.DateField()
    date_finished = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.viewer.name} watched {self.movie.title}"

class MovieViewer(models.Model):
    title = models.CharField(max_length=200)
    viewers = models.ManyToManyField(Viewer)

    def __str__(self):
        return self.title
