from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser
)

from post.models import Post
from post.serializers import PostSerializer
from post.permissions import MyIsAuthenticated, IsOwner


# Create your views here.
class PostPagination(PageNumberPagination):
    page_size = 100

class PostListView(ListCreateAPIView):
    queryset = Post.objects.select_related('user')
    serializer_class = PostSerializer
    permission_classes = [MyIsAuthenticated]
    pagination_class = PostPagination

    def get_queryset(self):
        return self.queryset


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]
    lookup_field = 'pk'