from django.db import models
from posts.models import Post

class Comment(models.Model):
  """Comment Model"""

  post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

  text = models.CharField(max_length=560)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '{} {}'.format(self.text, self.created_at)
    # return self