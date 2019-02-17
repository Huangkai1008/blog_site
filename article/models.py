from datetime import datetime

from django.db import models

__all__ = ['Article', 'Category', 'Tag']


class Category(models.Model):
    """
    博客-分类
    """
    name = models.CharField('分类名称', max_length=100)

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    博客-标签
    """
    name = models.CharField('标签名称', max_length=100)

    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# Create your models here.
class Article(models.Model):
    """
    博客-文章
    """
    title = models.CharField('文章标题', max_length=100, help_text='文章标题', unique=True)
    body = models.TextField('文章内容')
    create_time = models.DateTimeField('发布时间', default=datetime.now)
    update_time = models.DateTimeField('修改时间', auto_now=True)
    category = models.ForeignKey(Category, verbose_name='文章分类', on_delete=models.CASCADE, default='')
    tags = models.ManyToManyField(Tag, verbose_name='文章标签', blank=True)

    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
