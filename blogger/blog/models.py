from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    STATUS_OPTION = (("draft", "Draft"), ("published", "Published"))
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_OPTION, default="draft")

    class Meta:
        ordering = ("-create_at",)

    def __str__(self):
        return self.title
