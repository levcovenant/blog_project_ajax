from django.contrib import admin
from .models import Post, Photo

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['post', 'created']