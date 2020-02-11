# Generated by Django 3.0.2 on 2020-02-10 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment_alias', models.CharField(max_length=200, unique=True)),
                ('experiment_accession', models.CharField(max_length=200, unique=True)),
                ('experiment_title', models.CharField(max_length=200)),
                ('study_name', models.CharField(max_length=200)),
                ('design_description', models.TextField(max_length=200)),
                ('sample_accession', models.CharField(max_length=200)),
                ('sample_attribute', models.TextField(max_length=200)),
                ('library_strategy', models.CharField(max_length=200)),
                ('library_layout', models.CharField(max_length=200)),
                ('library_construction_protocol', models.TextField(max_length=200)),
                ('platform', models.CharField(max_length=200)),
                ('platform_parameters', models.CharField(max_length=200)),
                ('xref_link', models.CharField(max_length=200)),
                ('experiment_attribute', models.CharField(max_length=200)),
                ('submission_accession', models.CharField(max_length=200)),
                ('sradb_updated', models.CharField(max_length=200)),
                ('organism', models.CharField(max_length=200)),
                ('cell_line', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_accession', models.CharField(max_length=50, unique=True)),
                ('study_accession', models.CharField(max_length=50, unique=True)),
                ('study_title', models.CharField(blank=True, max_length=200)),
                ('study_type', models.CharField(blank=True, max_length=100)),
                ('study_abstract', models.TextField(blank=True)),
                ('study_description', models.CharField(blank=True, max_length=200)),
                ('xref_link', models.CharField(blank=True, max_length=200)),
                ('submission_accession', models.CharField(blank=True, max_length=50)),
                ('sradb_updated', models.CharField(blank=True, max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Srr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('sra_accession', models.CharField(max_length=50)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Experiment')),
            ],
        ),
        migrations.AddField(
            model_name='experiment',
            name='study',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Study'),
        ),
    ]