from django.urls import path, include
from rest_framework.routers import DefaultRouter

from members import views
from members.views import AllBooksAPI, MembersAPI

router = DefaultRouter()
router.register(r'books', AllBooksAPI)
router.register(r'members', MembersAPI)

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('<int:book_id>/add_to_list/', views.add_to_list, name='add_to_list'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('create_book/', views.create_book, name='create_book'),
    path('my_books/', views.my_books, name='my_books'),

    # API
    path('api/', include(router.urls)),
]
