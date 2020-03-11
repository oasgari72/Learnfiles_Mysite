from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Journal)
class JournalAdmin(admin.ModelAdmin):
    pass

class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance
    extra = 1

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre', 'display_journal']
    inlines = [BookInstanceInline]




@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
     list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
     fields  = [
        'first_name',
        'last_name',
        ('date_of_birth', 'date_of_death')
     ]

@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ['status', 'due_back']
    fieldsets = (
        ('None', {
            'fields':('book', 'imprint')
        }),
        ('availability',{
            'fields': ('status', 'due_back')
        })
    )
