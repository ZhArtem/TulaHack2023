from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'author', 
        'title', 
        # 'content', 
        'time_create', 
        'photo', 
        'category', 
        'theme', 
        'rating', 
        'is_moderated'
        )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_moderated',)
    list_filter = ('is_moderated', 'time_create')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)} 


class AuthorAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)} 


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Theme, ThemeAdmin)




