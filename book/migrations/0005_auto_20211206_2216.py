# Generated by Django 3.2.9 on 2021-12-06 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_rename_is_deleate_bookinfo_is_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peopleinfo',
            name='despriction',
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='description',
            field=models.CharField(max_length=100, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='commentcount',
            field=models.IntegerField(default=0, verbose_name='评论'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='name',
            field=models.CharField(max_length=10, unique=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='readcount',
            field=models.IntegerField(default=0, verbose_name='阅读量'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookinfo', verbose_name='图书'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'male'), (0, 'female')], default=1, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='name',
            field=models.CharField(max_length=10, unique=True, verbose_name='名称'),
        ),
    ]
