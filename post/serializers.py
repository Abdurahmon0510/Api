from rest_framework import serializers
from rest_framework.authtoken.admin import User

from olcha.serializers import UserSerializer
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_info = serializers.SerializerMethodField()

    def get_user_info(self, obj):
        user_info = {
            'username': obj.user.username,
            'user_id': obj.user.id,
            'is_staff': obj.user.is_staff,
        }
        return user_info
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
      user = UserSerializer(many=False, read_only=True)
      class Meta:
           model = User
           fields = '__all__'