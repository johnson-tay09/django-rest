from rest_framework import serializers
from .models import Post_two


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_two
        fields = ("id", "title", "author", "body")
