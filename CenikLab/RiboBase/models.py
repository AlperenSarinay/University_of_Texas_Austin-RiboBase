from django.db import models

# Create your models here.

class Study(models.Model):
    geo_accession = models.CharField(max_length = 200,unique=True,blank = False)
    def __str__(self):
        return self.geo_accession

class Experiment_show(models.Model):

    species = models.CharField(max_length = 200,blank=False)
    cellLine_Strain = models.CharField(max_length = 200)
    Cell_Tissue = models.CharField(max_length = 200)
    Dataset_Type= models.CharField(max_length = 200,blank=False)
    SRA_Accession= models.CharField(max_length = 200,blank=False)
    Instrument= models.CharField(max_length = 200, unique=True,blank=False) 
    create_date = models.DateTimeField(auto_now_add = True) 
    Geo= models.ForeignKey(Study, blank=False, on_delete=models.CASCADE,related_name = "Study_num")
    def __str__(self):
        return self.species
class MetaData(models.Model):
    experiment = models.ForeignKey(Experiment_show,blank=False, on_delete=models.CASCADE,related_name="metadata")
    Status = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 200,blank=False)
    SampleType= models.CharField(max_length = 200,blank=False)
    SourceName = models.CharField(max_length = 200,blank=False)
    Organizm = models.TextField(blank=False)
    Characteristics = models.TextField(blank=False)
    GrowthProtocol = models.TextField(blank=False)
    ExtractedMolecule = models.CharField(max_length=200,blank=False)
    ExtractionProtocol = models.TextField(blank=False)
    LibraryStrategy = models.CharField(max_length=200,blank=False)
    LibrarySource = models.CharField(max_length=200,blank=False)
    LibrarySelection = models.CharField(max_length=200,blank=False)
    InstrumentModel = models.CharField(max_length=200,blank=False)
    Description = models.CharField(max_length=200,blank=False)  




