# Generated by Django 3.2.18 on 2023-06-14 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='views',
            new_name='view_count',
        ),
        migrations.AlterField(
            model_name='post',
            name='address',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='place_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]