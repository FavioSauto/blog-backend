from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = CommentSerializer