# Generated by Django 2.1.8 on 2019-05-02 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20190502_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='DockerContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('end_datetime', models.DateTimeField(verbose_name='结束时间')),
                ('container_id', models.CharField(max_length=128, verbose_name='容器ID')),
                ('container_url', models.CharField(max_length=128, verbose_name='容器映射出来的链接')),
                ('Pinguser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.PingUser')),
            ],
            options={
                'abstract': False,
                'verbose_name': '记录日期',
            },
        ),
        migrations.CreateModel(
            name='DockerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('end_datetime', models.DateTimeField(verbose_name='结束时间')),
                ('repositiry', models.CharField(max_length=128, verbose_name='镜像名称')),
                ('tag', models.CharField(max_length=128, verbose_name='镜像标签')),
                ('size', models.CharField(max_length=128, verbose_name='镜像大小')),
            ],
            options={
                'abstract': False,
                'verbose_name': '记录日期',
            },
        ),
        migrations.AddField(
            model_name='dockercontainer',
            name='image_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DockerImage'),
        ),
    ]
