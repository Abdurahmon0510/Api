from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book


# Create your views here.
def index(request):
    data = {
        'message': 'Success',
        'status_code': 201,
        'user': 'john'
    }
    return JsonResponse(data)


class UserList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        # usernames = [user.username for user in User.objects.all()]
        data = [
            {
                user.username:
                    {
                        'username': user.username,
                        'is_active': user.is_active,
                        'is_staff': user.is_staff

                    }
            }
            for user in User.objects.all()
        ]
        return Response({'data': data})


class BookListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        book_list = []

        for book in books:
            book_data = {
                book.title: {
                    "published_date": book.published_date,
                    "pages": book.pages,
                    "cover_image": book.cover_image.url if book.cover_image else None,
                    "description": book.description
                }
            }
            book_list.append(book_data)

        return Response(book_list, status=status.HTTP_200_OK)
