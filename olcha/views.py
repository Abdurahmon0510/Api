# from django.contrib.auth.models import User
# from django.http import JsonResponse
# from rest_framework import status
#
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from olcha.models import Book
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

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
#         for olcha in books:
#             book_data = {
#                 olcha.title: {
#                     "published_date": olcha.published_date,
#                     "pages": olcha.pages,
#                     "cover_image": olcha.cover_image.url if olcha.cover_image else None,
#                     "description": olcha.description
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

from .models import Category, Group, Product
from .serializers import CategorySerializer, ProductSerializer, GroupSerializer


#
# class CategoryListCreateView(APIView):
#
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CategoryDetailView(APIView):
#
#     def get(self, request, pk):
#         try:
#             category = Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         try:
#             category = Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         try:
#             category = Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListCreateView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class GroupListCreateView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Group.objects.filter(category__slug=category_slug)


class GroupDetailView(RetrieveDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'slug'


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(APIView):
     parser_classes = [MultiPartParser, FormParser]

     def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def get_queryset(self):
        group_slug = self.kwargs['group_slug']
        return Product.objects.filter(group__slug=group_slug)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
