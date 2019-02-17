from django.contrib import admin

# Register your models here.
from .models import Article, Tag, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    文章admin
    """
    fields = ('title', 'body', 'create_time', 'category', 'tags')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    分类admin
    """
    fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    标签admin
    """
    fields = ('name',)
