from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=8000)
    publish_date = models.DateTimeField(auto_now_add=True)

class Tags(models.Model):
    text = models.CharField(max_length=1000)
    blogPost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)