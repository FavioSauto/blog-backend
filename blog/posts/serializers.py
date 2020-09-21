from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
  comments = serializers.StringRelatedField(many=True, required=False)

  class Meta:
    model = Post
    fields = ['id', 'title', 'body', 'created_at', 'comments']

  def create(self, validated_data):
    """Create and return a new 'Post', given the validated data."""

    return Post.objects.create(**validated_data)

  def update(self, instance, validated_data):
    """Update and return an existing 'Post' instance, given the validated data."""

    instance.title = validated_data.get('title', instance.title)
    instance.body = validated_data.get('body', instance.body)
    instance.save()

    return instance
    