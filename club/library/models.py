from django.db import models

from members.models import MemberCard


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    book_available = models.BooleanField(default=True)

    members_books = models.ForeignKey(
        MemberCard, on_delete=models.SET_NULL,
        related_name='book_set', blank=True, null=True)
    was_read = models.ManyToManyField(
        MemberCard, related_name='read_books', blank=True)

    def __str__(self):
        return self.title
