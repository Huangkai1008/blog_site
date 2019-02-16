# -*- coding:utf-8 -*-
from rest_framework import serializers

from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """文章序列化器"""
    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'create_time', 'update_time')