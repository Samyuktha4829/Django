from django.contrib import admin
from testapp.models import Movie
# Register your models here.
class admin_movie(admin.ModelAdmin):
    list_display=['mdate','moviename','hero','heroin','review']
admin.site.register(Movie, admin_movie)