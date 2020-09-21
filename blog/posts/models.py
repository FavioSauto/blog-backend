from django.db import models

class Post(models.Model):
  """Post Model"""

  title = models.CharField(max_length=140)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    """Return title"""
    return self.title