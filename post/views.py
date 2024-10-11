from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.defaults import page_not_found
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
    ordering = 'created'

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [MyIsAuthenticated]
    pagination_class = PostPagination

    def get_queryset(self):
        cache_key = 'post-list'
        cached_data = cache.get(cache_key)
        if not cached_data:
            queryset = Post.objects.select_related('user') \
                .prefetch_related('user__groups') \
                .prefetch_related('user__user_permissions')
            cached_data = list(queryset)
            cache.set(cache_key, cached_data, timeout=300)
            return cached_data
        return cached_data



class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]
    lookup_field = 'pk'

