# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class Description(models.Model):
    """博客类别"""
    description = models.CharField(verbose_name="分类", max_length=20)
    text = models.CharField(verbose_name="简介", max_length=100, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"


class Blog(models.Model):
    """博客信息"""
    title = models.CharField(verbose_name="标题", max_length=50)
    id = models.AutoField(verbose_name="id", primary_key=True)
    text = UEditorField("内容", height=300, width=1000,
                        default='在此输入', blank=True, imagePath="uploads/images/",
                        toolbars='besttome', filePath='uploads/files/')
    comment = models.TextField(verbose_name="评论", blank=True, null=True)
    clicks = models.IntegerField(verbose_name="点击量", default=0)
    datetime = models.DateTimeField(verbose_name="提交时间", auto_now=True)
    # time = models.TimeField(verbose_name="提交时间", default=now)
    description = models.ManyToManyField(Description, verbose_name="分类")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = "博客"
