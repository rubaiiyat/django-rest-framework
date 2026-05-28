from django.db import models

# Create your models here.

class BlogsModel(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()

    def __str__(self):
        return self.title


class CommentsModel(models.Model):
    blog=models.ForeignKey(BlogsModel, on_delete=models.CASCADE,related_name='comments')
    comment=models.CharField(max_length=200)

    def __str__(self):
        return self.comment