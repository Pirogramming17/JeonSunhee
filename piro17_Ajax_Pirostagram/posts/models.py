from django.db import models

# Create your models here.
class Post(models.Model):
    like = models.BooleanField(default=False)

class Reply(models.Model):
    # author = models.CharField(max_length=100)
    content = models.TextField()