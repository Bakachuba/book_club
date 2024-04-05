from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from library.models import Book
from members.forms import BooksForm
from members.models import MemberCard
from members.serializers import BooksSerializer, MemberCardSerializer


# Вывод всех книг
def all_books(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'members/all_books.html',
                  {'books': books})


@login_required
def like_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(pk=book_id)
        book.likes.add(request.user.membercard)  # Add the user's MemberCard to the likes

        books = Book.objects.all().order_by('-id')
        return render(request, 'members/all_books.html', {'books': books})

    return redirect('all_books')

# Создание книги
@login_required
def create_book(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            books = form.save(commit=False)
            books.user = request.user
            books.save()
            return redirect('all_books')
    else:
        form = BooksForm

    return render(request, 'members/create_form.html',
                  {'form': form})


# Update книги (пользователь арендует книгу)
@login_required
def add_to_list(request, book_id):
    book = Book.objects.get(pk=book_id)

    book.book_available = False
    book.members_books = request.user.membercard
    book.save()

    return redirect('all_books')


# Удаление книги
@login_required
def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('all_books')


# Список книг, которые пользователь арендовал
# POST Запрос на возвращение книги
@login_required
def my_books(request):
    user = request.user
    user_books = Book.objects.filter(members_books=user.membercard,
                                     book_available=False)

    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = Book.objects.get(pk=book_id)
        book.book_available = True
        book.save()

    return render(request, 'members/m_books.html',
                  {'user_books': user_books})


# Доступ к API только авторизованным пользователям
class AllBooksAPI(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]


class MembersAPI(viewsets.ReadOnlyModelViewSet):
    queryset = MemberCard.objects.all()
    serializer_class = MemberCardSerializer
    permission_classes = [IsAuthenticated]