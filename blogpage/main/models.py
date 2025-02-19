from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Tags(models.Model):
    text = models.CharField(max_length=255, unique=True)
    blogPost = models.ManyToManyField(BlogPost, related_name="tags") # Blogpost can have multiple tags, tags can be linked to multiple blogpost 

    def __str__(self):
        return self.text

#TODO: figure out how to use the info from UI in DB