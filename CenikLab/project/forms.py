from django import forms
from .models import Experiment,Study,Srr


class AddExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ["study","experiment_alias","experiment_accession","experiment_title","study_name","design_description","sample_accession","sample_attribute",
                  "library_strategy","library_layout","library_construction_protocol","platform","platform_parameters","xref_link",
                  "experiment_attribute","submission_accession","sradb_updated","organism","cell_line","experiment_file"]

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ["organism","cell_line"]    


class AddStudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields =["geo_accession","study_accession","study_title","study_type","study_abstract","study_description","xref_link",
        "submission_accession","sradb_updated"]


class AddSrrForm(forms.ModelForm):
    class Meta:
        model = Srr
        fields = ["experiment","sra_accession"]


       




