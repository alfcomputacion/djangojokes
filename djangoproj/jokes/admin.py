from django.contrib import admin
from .models import Category, Joke

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('slug', 'created', 'updated')
        return ()


@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    model = Joke

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('slug', 'created', 'updated')
        return ()
