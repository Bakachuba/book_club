from django import forms

from library.models import Book


class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date',
                  'book_available', 'members_books', 'was_read']
        labels = {
            'title': 'Название'
        }