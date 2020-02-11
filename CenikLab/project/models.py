from django.db import models


# Create your models here.

class Study(models.Model):

    geo_accession = models.CharField( max_length = 50,unique = True,blank = False)
    study_accession = models.CharField(max_length = 50,unique = True,blank = False)
    study_title = models.CharField(max_length = 200,unique = False,blank = True)
    study_type = models.CharField(max_length = 100,unique = False,blank = True)
    study_abstract = models.TextField(blank = True)
    study_description = models.CharField(max_length = 200,unique = False,blank = True)
    xref_link = models.CharField(max_length = 200,unique = False,blank = True)
    submission_accession = models.CharField(max_length = 50,unique = False,blank = True)
    sradb_updated = models.CharField(max_length = 200,unique = False,blank = True)
    create_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.geo_accession


class Experiment(models.Model):

    study = models.ForeignKey('Study',blank = False,on_delete = models.CASCADE)
    experiment_alias = models.CharField(max_length = 200,unique = True,blank = False)
    experiment_accession = models.CharField(max_length = 200,unique = True,blank = False)
    experiment_title = models.CharField(max_length = 200,blank = False)
    study_name = models.CharField(max_length = 200,blank = False)
    design_description = models.TextField(max_length = 200,blank = False)
    sample_accession = models.CharField(max_length = 200,blank = False)
    sample_attribute = models.TextField(max_length = 200,blank = False)
    library_strategy = models.CharField(max_length = 200,blank = False)
    library_layout = models.CharField(max_length = 200,blank = False)
    library_construction_protocol = models.TextField(max_length = 200,blank = False)
    platform = models.CharField(max_length = 200,blank = False)
    platform_parameters = models.CharField(max_length = 200,blank = False)
    xref_link = models.CharField(max_length = 200,blank = False)
    experiment_attribute = models.CharField(max_length = 200,blank = False)
    submission_accession = models.CharField(max_length = 200,blank = False)
    sradb_updated = models.CharField(max_length = 200,blank = False)
    organism = models.CharField(max_length = 200,blank = False)
    cell_line = models.CharField(max_length = 200,blank = False)    
    create_date = models.DateTimeField(auto_now_add = True) 

    def __str__(self):
        return self.experiment_alias

class Srr(models.Model):
    experiment = models.ForeignKey('Experiment',blank=False,on_delete = models.CASCADE)
    create_date = models.DateTimeField(auto_now_add = True)
    sra_accession = models.CharField(max_length = 50,blank = False)
    def __str__(self):
        return self.sra_accession




