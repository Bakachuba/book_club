from django.db import models

from members.models import MemberCard


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    book_available = models.BooleanField(default=True)

    members_books = models.ForeignKey(MemberCard, on_delete=models.CASCADE, related_name='book_set')
    was_read = models.ManyToManyField(MemberCard, related_name='read_books')

    def __str__(self):
        return self.title
