# Generated by Django 3.0.2 on 2020-02-11 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200211_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='experiment_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
