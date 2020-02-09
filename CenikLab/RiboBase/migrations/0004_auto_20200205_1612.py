# Generated by Django 3.0.2 on 2020-02-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiboBase', '0003_auto_20200205_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment_show',
            name='Cell_Tissue',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='experiment_show',
            name='Dataset_Type',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='experiment_show',
            name='Geo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='experiment_show',
            name='SRA_Accession',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='experiment_show',
            name='cellLine_Strain',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='experiment_show',
            name='species',
            field=models.CharField(max_length=200),
        ),
    ]
