# -*- coding:utf-8 -*-
from rest_framework import serializers

from article.models import Article, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    """
    文章分类序列化器
    """

    class Meta:
        model = Category
        fields = ('name',)


class TagSerializer(serializers.ModelSerializer):
    """
    文章标签序列化器
    """

    class Meta:
        model = Tag
        fields = ('name',)


class ArticleSerializer(serializers.ModelSerializer):
    """文章序列化器"""
    category = serializers.CharField(source='category.name')
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'create_time', 'update_time', 'category', 'tags')
