from django.urls import reverse
from django.db import models

# Create your models here.


class Joke(models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, editable=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:detail', args=[self.slug])

    def __str__(self):
        return self.question
