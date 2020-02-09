from django import forms
from .models import MetaData,Experiment_show


class AddExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment_show
        fields = ["species","cellLine_Strain","Cell_Tissue","Dataset_Type","SRA_Accession","Instrument","Geo"]

class AddDataForm(forms.ModelForm):
    class Meta:
        model = MetaData
        fields = ["title","SampleType","SourceName","Organizm","Characteristics","GrowthProtocol","ExtractedMolecule",
        "ExtractionProtocol","LibraryStrategy","LibrarySource","LibrarySelection","InstrumentModel","Description","experiment"] 


                 
        


       

       
   
    
        
        