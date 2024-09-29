from django.contrib.auth.models import User
from django.db.models import Avg
from rest_framework import serializers
from .models import Category, Group, Product, Image, Comment, ProductAttribute, AttributeKey, AttributeValue


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


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = '__all__'


class AttributeKeySerializer(serializers.ModelSerializer):
    values = AttributeValueSerializer(many=True, read_only=True)

    class Meta:
        model = AttributeKey
        fields = '__all__'


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        exclude = ('id','product','attr_key','attr_value')

    def to_representation(self, instance):
        context = super(ProductAttributeSerializer, self).to_representation(instance)
        context['key_id'] = instance.attr_key.id
        context['key_name'] = instance.attr_key.key_name

        context['value_id'] = instance.attr_value.id
        context['value_name'] = instance.attr_value.value_name
        return context
class ProductSerializer(serializers.ModelSerializer):
    # images = ProductImageSerializer(many=True, read_only=True)
    attributes = ProductAttributeSerializer(many=True,read_only=True)

    all_images = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    users_like = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    def get_all_images(self, obj):
        all_images = []
        images = obj.images.all()
        request = self.context.get('request')
        for image in images:
            all_images.append(request.build_absolute_uri(image.image.url))
        return all_images

    def get_comments(self, obj):
        comments = Comment.objects.filter(product=obj)
        return [{"user": comment.user.username, "message": comment.message} for comment in comments]

    def get_comments_count(self, obj):
        return Comment.objects.filter(product=obj).count()

    def get_users_like(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.users_like.filter(
                id=request.user.id).exists()
        return False

    def get_rating(self, obj):
        comments = Comment.objects.filter(product=obj)
        if comments.exists():
            return comments.aggregate(average_rating=Avg('rating'))['average_rating']
        return 0


    class Meta:
        model = Product
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user