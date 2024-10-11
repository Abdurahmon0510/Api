from rest_framework import serializers
from django.contrib.auth.models import User

from olcha.serializers import UserSerializer
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_info = serializers.SerializerMethodField()

    def get_user_info(self, obj):
        return {
            'username': obj.user.username,
            'user_id': obj.user.id,
            'is_staff': obj.user.is_staff,
        }

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user']

class UsersSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'