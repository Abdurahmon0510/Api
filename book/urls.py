
from django.contrib import admin
from django.urls import path

from book import views
from book.views import CategoryListCreateView, CategoryDetailView

urlpatterns = [
    # path('index/',views.index,name='index'),
    # path('users/',views.UserList.as_view(),name='users'),
    # path('books/',views.BookListAPIView.as_view(),name='books'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]
