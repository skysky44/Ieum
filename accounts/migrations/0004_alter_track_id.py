# Generated by Django 3.2.18 on 2023-05-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_track_is_selected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]