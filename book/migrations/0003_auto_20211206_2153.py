# Generated by Django 3.2.9 on 2021-12-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20211202_2150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={},
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='despriction',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'male'), (0, 'female')], default=1),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterModelTable(
            name='peopleinfo',
            table='peopleinfo',
        ),
    ]
