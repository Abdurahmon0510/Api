
from django.contrib import admin
from django.urls import path

from book import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('users/',views.UserList.as_view(),name='users'),
    path('books/',views.BookListAPIView.as_view(),name='books'),
]
