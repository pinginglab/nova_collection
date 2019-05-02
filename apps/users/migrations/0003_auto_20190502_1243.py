# Generated by Django 2.1.8 on 2019-05-02 04:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190502_1135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pinguser',
            options={'default_permissions': (), 'permissions': (('select_user', '查看用户'), ('change_user', '修改用户'), ('delete_user', '删除用户')), 'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AddField(
            model_name='pinguser',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pinguser',
            name='fullname',
            field=models.CharField(max_length=64, null=True, verbose_name='中文名'),
        ),
        migrations.AddField(
            model_name='pinguser',
            name='phonenumber',
            field=models.CharField(max_length=16, null=True, unique=True, verbose_name='电话'),
        ),
        migrations.AddField(
            model_name='pinguser',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]