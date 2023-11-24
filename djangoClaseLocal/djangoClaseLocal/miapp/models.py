from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, default="")
    content = models.TextField()
    public = models.BooleanField()
    autor = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


