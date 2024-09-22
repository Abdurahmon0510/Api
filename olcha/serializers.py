from rest_framework import serializers
from .models import Category, Group, Product


class CategorySerializer(serializers.ModelSerializer):
    full_image_url = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField(method_name='groups_count')

    def groups_count(self, obj):
        count = obj.groups.count()
        return count

    def get_full_image_url(self, instance):

        if instance.image:
            image_url = instance.image.url
            request = self.context.get('request')
            return request.build_absolute_uri(image_url)
        else:
            return None

    class Meta:
        model = Category
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    full_image_url = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField(method_name='products_count')

    def products_count(self, obj):
        count = obj.products.count()
        return count

    def get_full_image_url(self, instance):
        if instance.image:
            image_url = instance.image.url
            request = self.context.get('request')
            return request.build_absolute_uri(image_url)
        else:
            return None

    class Meta:
        model = Group
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    full_image_url = serializers.SerializerMethodField()

    def get_full_image_url(self, instance):

        if instance.image:
            image_url = instance.image.url
            request = self.context.get('request')
            return request.build_absolute_uri(image_url)
        else:
            return None

    class Meta:
        model = Product
        fields = '__all__'
