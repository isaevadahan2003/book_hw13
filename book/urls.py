from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_all, name='books'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('add-book/', views.add_book, name='add_book'),
    path('shows/<int:id>/update/', views.book_update, name='book_update'),
    path('shows/<int:id>/delete/', views.book_delete, name='book_delete'),
]