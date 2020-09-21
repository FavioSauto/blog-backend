from rest_framework import routers
from .api import PostViewSet
from comments.api import CommentViewSet

router = routers.DefaultRouter()
router.register('api/posts', PostViewSet, 'posts')
router.register('api/comments', CommentViewSet, 'comments')

urlpatterns = router.urls