from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name

class Journal(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book Journal")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'title')
    summary = models.TextField(max_length=1500, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=20, help_text='20 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    journal = models.ManyToManyField(Journal)

    def display_genre (self):
        return ', '.join([genre.name for genre in self.genre.all()[:]])

    def display_journal (self):
        return ', '.join([journal.name for journal in self.journal.all()[:]])

    display_genre.short_description = 'Genre'
    display_journal.short_description = 'Journal'

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200, blank = True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1,
                        choices=LOAN_STATUS,
                        blank=True, default='m',
                        help_text='Book availability')

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
            ordering = ["due_back"]


    def __str__(self):
        return '{0},{1}'.format(self.id,self.book.title)
