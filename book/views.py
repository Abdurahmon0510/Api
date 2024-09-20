# from django.contrib.auth.models import User
# from django.http import JsonResponse
# from rest_framework import status
#
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from book.models import Book

# # Create your views here.
# def index(request):
#     data = {
#         'message': 'Success',
#         'status_code': 201,
#         'user': 'john'
#     }
#     return JsonResponse(data)
#
#
# class UserList(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         # usernames = [user.username for user in User.objects.all()]
#         data = [
#             {
#                 user.username:
#                     {
#                         'username': user.username,
#                         'is_active': user.is_active,
#                         'is_staff': user.is_staff
#
#                     }
#             }
#             for user in User.objects.all()
#         ]
#         return Response({'data': data})
#
#
# class BookListAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         books = Book.objects.all()
#         book_list = []
#
#         for book in books:
#             book_data = {
#                 book.title: {
#                     "published_date": book.published_date,
#                     "pages": book.pages,
#                     "cover_image": book.cover_image.url if book.cover_image else None,
#                     "description": book.description
#                 }
#             }
#             book_list.append(book_data)
#
#         return Response(book_list, status=status.HTTP_200_OK)
#
#
# class BookCreateAPIView(APIView):
#       def get(self,request):
#           books = Book.objects.all()
#           serializer = BookSerializer(books, many=True)
#           return Response(serializer.data, status=status.HTTP_200_OK)
#
#       def post(self,request):
#           serializer = BookSerializer(data=request.data)
#           if serializer.is_valid():
#               serializer.save()
#               data = {
#                   'success': True,
#                   'message': 'Book created successfully',
#               }
#               return JsonResponse(data, status=status.HTTP_201_CREATED)
#           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer


class CategoryListCreateView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
