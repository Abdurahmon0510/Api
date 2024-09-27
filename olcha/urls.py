
from django.urls import path
from olcha.views import CategoryListCreateView, CategoryDetailView, ProductDetailView, \
    GroupListCreateView, GroupDetailView, ProductListCreateView, ProductCreateAPIView, AllProductsView, \
    ImageListApiView, AttributeKeyListCreateView, AttributeValueListCreateView, ProductAttributeListCreateView

urlpatterns = [
    path('api/category/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('api/category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('api/category/<slug:category_slug>/group/', GroupListCreateView.as_view(), name='group_list_create'),
    path('api/category/<slug:category_slug>/group/<slug:slug>/', GroupDetailView.as_view(), name='group_detail'),
    path('api/category/<slug:category_slug>/group/<slug:group_slug>/product/', ProductListCreateView.as_view(),
         name='product_list_create'),
    path('api/category/<slug:category_slug>/group/<slug:group_slug>/product/<slug:slug>/', ProductDetailView.as_view(),
         name='product_detail'),
    path('productcreate/', ProductCreateAPIView.as_view(), name='product_create'),
    path('all-products/', AllProductsView.as_view(), name='all_products'),
    path('all-images/', ImageListApiView.as_view(), name='all_images'),
    path('api/attribute-keys/', AttributeKeyListCreateView.as_view(), name='attribute_key_list_create'),
    path('api/attribute-values/', AttributeValueListCreateView.as_view(), name='attribute_value_list_create'),
    path('api/product-attributes/', ProductAttributeListCreateView.as_view(), name='product_attribute_list_create')

]
