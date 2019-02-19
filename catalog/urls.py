from django.urls import path ,include
from . import views

app_name='catalog'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int : pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<int : pk>/renew/', views.renew_book_librarian, name='renew-book-librarian')
]
