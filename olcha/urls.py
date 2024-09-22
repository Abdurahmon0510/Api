
from django.urls import path
from olcha.views import CategoryListCreateView, CategoryDetailView, ProductDetailView, \
    GroupListCreateView, GroupDetailView, ProductListCreateView, ProductCreateAPIView

urlpatterns = [
    path('api/category/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('api/category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('api/category/<slug:category_slug>/group/', GroupListCreateView.as_view(), name='group_list_create'),
    path('api/category/<slug:category_slug>/group/<slug:slug>/', GroupDetailView.as_view(), name='group_detail'),
    path('api/category/<slug:category_slug>/group/<slug:group_slug>/product/', ProductListCreateView.as_view(), name='product_list_create'),
    path('api/category/<slug:category_slug>/group/<slug:group_slug>/product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('productcreate/',ProductCreateAPIView.as_view(), name='product_create'),

]
