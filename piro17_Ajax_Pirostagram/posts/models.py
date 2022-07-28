from django.db import models

# Create your models here.
class Post(models.Model):
    like = models.BooleanField(default=False)

class Reply(models.Model):
    content = models.TextField()