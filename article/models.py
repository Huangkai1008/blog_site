from datetime import datetime

from django.db import models


# Create your models here.
class Article(models.Model):
    """
    博客-文章
    """
    title = models.CharField('文章标题', max_length=100, help_text='文章标题', unique=True)
    body = models.TextField('文章内容')
    create_time = models.DateTimeField('发布时间', default=datetime.now)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
