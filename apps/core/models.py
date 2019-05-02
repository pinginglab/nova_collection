from django.db import models
from django.db.models import CASCADE

from apps.users.models import PingUser


class Base(models.Model):
    class Meta:
        abstract = True
        verbose_name = "记录日期"

    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    end_datetime = models.DateTimeField(verbose_name="结束时间")


class DockerImage(Base):
    repositiry = models.CharField(max_length=128, null=False, verbose_name='镜像名称')
    tag = models.CharField(max_length=128, null=False, verbose_name='镜像标签')
    size = models.CharField(max_length=128, null=False, verbose_name='镜像大小')


class DockerContainer(Base):
    image_name = models.ForeignKey(DockerImage, on_delete=CASCADE)
    container_id = models.CharField(max_length=128, null=False, verbose_name='容器ID')
    Pinguser = models.ForeignKey(PingUser, on_delete=CASCADE)
    container_url = models.CharField(max_length=128, null=False, verbose_name='容器映射出来的链接')
