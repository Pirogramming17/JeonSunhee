from django.db import models

# Create your models here.
class Devtool(models.Model):
    name = models.CharField(max_length=50, verbose_name="이름")
    kind = models.CharField(max_length=50, verbose_name="종류")
    descript = models.TextField(verbose_name="설명")

class IdeaStart(models.Model):
    star = models.IntegerField(verbose_name="찜하기")

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    image = models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name="이미지")
    content = models.TextField(verbose_name="컨텐츠")
    interest = models.IntegerField(verbose_name="관심도")
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, related_name="post_devtool")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    