from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
