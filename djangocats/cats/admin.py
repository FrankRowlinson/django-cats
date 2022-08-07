from django.contrib import admin
from .models import *


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_created', 'time_edited', 'is_public')
    list_display_links = ('title',)
    search_fields = ('title', 'description', 'is_public')
    list_editable = ('is_public', )
    list_filter = ('is_public', 'time_created')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


admin.site.register(Cat, CatAdmin)
admin.site.register(Category, CategoryAdmin)
