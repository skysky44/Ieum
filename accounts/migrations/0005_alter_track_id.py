# Generated by Django 3.2.18 on 2023-05-26 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_track_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]