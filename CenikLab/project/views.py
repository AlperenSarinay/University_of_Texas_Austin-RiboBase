from django.shortcuts import render,redirect,get_object_or_404
from .models import Experiment,Study
from .forms import AddExperimentForm,AddStudyForm,AddSrrForm
from django.contrib import messages

# Create your views here.

def index(request):
    
    experiments = Experiment.objects.all()
    
    return render(request,"index.html",{"experiments":experiments})

def about(request):
    return render(request,"about.html")

def DataSearch(request):

    keyword_Organism = request.GET.get("keyword_organism")
    keyword_Study = request.GET.get("keyword_study")
    keyword_Cell_line = request.GET.get("keyword_cell_line")
    keyword_Title = request.GET.get("keyword_experiment_title")
    keyword_Accession = request.GET.get("keyword_experiment_accession")
    keyword_sra = request.GET.get("keyword_sample_accession")
    keyword_Attribute = request.GET.get("keyword_experiment_attribute")

    if keyword_Organism:
        experiments = Experiment.objects.filter(organism__contains=keyword_Organism)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_Study:
        study = Study.objects.get(geo_accession=keyword_Study)
        experiments = Experiment.objects.filter(study__geo_accession = study.geo_accession)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_Cell_line:
        experiments = Experiment.objects.filter(cell_line__contains=keyword_Cell_line)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_Title:
        experiments = Experiment.objects.filter(experiment_title__contains=keyword_Title)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_Accession:
        experiments = Experiment.objects.filter(experiment_accession__contains=keyword_Accession)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_sra:
        experiments = Experiment.objects.filter(sample_accession__contains=keyword_sra)
        return render(request,"DataSearch.html",{"experiments":experiments}) 
        
    if keyword_Attribute:
        experiments = Experiment.objects.filter(experiment_attribute__contains=keyword_Attribute)
        return render(request,"DataSearch.html",{"experiments":experiments})   

    experiments = Experiment.objects.all()
    return render(request,"DataSearch.html",{"experiments":experiments})

def DataDownload(request):

    keyword_Organism = request.GET.get("keyword_organism")
    keyword_Study = request.GET.get("keyword_study")
    keyword_Cell_line = request.GET.get("keyword_cell_line")
    keyword_Title = request.GET.get("keyword_experiment_title")
    keyword_Accession = request.GET.get("keyword_experiment_accession")
    keyword_sra = request.GET.get("keyword_sample_accession")
    keyword_Attribute = request.GET.get("keyword_experiment_attribute")

    if keyword_Organism:
        experiments = Experiment.objects.filter(organism__contains=keyword_Organism)
        return render(request,"DataDownload.html",{"experiments":experiments})

    if keyword_Study:
        study = Study.objects.get(geo_accession=keyword_Study)
        experiments = Experiment.objects.filter(study__geo_accession = study.geo_accession)
        return render(request,"DataDownload.html",{"experiments":experiments})

    if keyword_Cell_line:
        experiments = Experiment.objects.filter(cell_line__contains=keyword_Cell_line)
        return render(request,"DataDownload.html",{"experiments":experiments})

    if keyword_Title:
        experiments = Experiment.objects.filter(experiment_title__contains=keyword_Title)
        return render(request,"DataDownload.html",{"experiments":experiments})

    if keyword_Accession:
        experiments = Experiment.objects.filter(experiment_accession__contains=keyword_Accession)
        return render(request,"DataDownload.html",{"experiments":experiments})

    if keyword_sra:
        experiments = Experiment.objects.filter(sample_accession__contains=keyword_sra)
        return render(request,"DataDownload.html",{"experiments":experiments}) 
        
    if keyword_Attribute:
        experiments = Experiment.objects.filter(experiment_attribute__contains=keyword_Attribute)
        return render(request,"DataDownload.html",{"experiments":experiments})   

    
    experiments = Experiment.objects.all()
    return render(request,"DataDownload.html",{"experiments":experiments})

def AddExperiment(request):
    form= AddStudyForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"The Experiment was successfully created.")
        return redirect("AddExperiment")
    return render(request,"AddExperiment.html",{"form":form})
    

def addData(request):

    form = AddExperimentForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request,"The Experiment was successfully created.")
        return redirect("addData")
        
    return render(request,"addData.html",{"form":form})

def DataSearchPage(request,id):
    
    experiments = Experiment.objects.filter(id=id).all()
    
    
    return render(request,"DataSearchPage.html",{"experiments":experiments})

def Comparasion(request):

    keyword_Organism = request.GET.get("keyword_organism")
    keyword_Study = request.GET.get("keyword_study")
    keyword_Cell_line = request.GET.get("keyword_cell_line")
    keyword_Title = request.GET.get("keyword_experiment_title")
    keyword_Accession = request.GET.get("keyword_experiment_accession")
    keyword_sra = request.GET.get("keyword_sample_accession")
    keyword_Attribute = request.GET.get("keyword_experiment_attribute")

    if keyword_Organism:
        experiments = Experiment.objects.filter(organism__contains=keyword_Organism)
        return render(request,"Comparasion.html",{"experiments":experiments})

    if keyword_Study:
        study = Study.objects.get(geo_accession=keyword_Study)
        experiments = Experiment.objects.filter(study__geo_accession = study.geo_accession)
        return render(request,"Comparasion.html",{"experiments":experiments})

    if keyword_Cell_line:
        experiments = Experiment.objects.filter(cell_line__contains=keyword_Cell_line)
        return render(request,"Comparasion.html",{"experiments":experiments})

    if keyword_Title:
        experiments = Experiment.objects.filter(experiment_title__contains=keyword_Title)
        return render(request,"Comparasion.html",{"experiments":experiments})

    if keyword_Accession:
        experiments = Experiment.objects.filter(experiment_accession__contains=keyword_Accession)
        return render(request,"Comparasion.html",{"experiments":experiments})

    if keyword_sra:
        experiments = Experiment.objects.filter(sample_accession__contains=keyword_sra)
        return render(request,"Comparasion.html",{"experiments":experiments}) 
        
    if keyword_Attribute:
        experiments = Experiment.objects.filter(experiment_attribute__contains=keyword_Attribute)
        return render(request,"Comparasion.html",{"experiments":experiments})   


    experiments = Experiment.objects.all()
    return render(request,"Comparasion.html",{"experiments":experiments})

def UpdateExperiment(request,id):

    experiments = get_object_or_404(Experiment,id=id)
    form = AddExperimentForm(request.POST or None,instance = experiments)
    if form.is_valid():
        experiments = form.save(commit=False)
        experiments.save()
        messages.success(request,"The Experiment was successfully update.")
        return redirect("DataSearchPage")

    return render(request,"Update.html",{"form":form})

def AddSRR(request):

    form = AddSrrForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"The SRR  was successfully created.")
        return redirect("AddSRR")
        
    return render(request,"AddSRR.html",{"form":form})

def StudySearch(request):

    keyword_Accession = request.GET.get("keyword_accession")
    keyword_Title = request.GET.get("keyword_title")
    keyword_Type = request.GET.get("keyword_type")
    keyword_Abstract= request.GET.get("keyword_abstract")
    keyword_Description = request.GET.get("keyword_Description")
    keyword_Geo = request.GET.get("keyword_geo")
    
    if keyword_Accession:
        studies = Study.objects.filter(study_accession__contains=keyword_Accession)
        return render(request,"StudySearch.html",{"studies":studies})

    if keyword_Title:
        studies = Study.objects.filter(study_title__contains=keyword_Title)
        return render(request,"StudySearch.html",{"studies":studies})

    if keyword_Type:
        studies = Study.objects.filter(study_type__contains=keyword_Type)
        return render(request,"StudySearch.html",{"studies":studies})

    if keyword_Abstract:
        studies = Study.objects.filter(study_abstract__contains=keyword_Abstract)
        return render(request,"StudySearch.html",{"studies":studies})

    if keyword_Description:
        studies = Study.objects.filter(study_description__contains=keyword_Description)
        return render(request,"StudySearch.html",{"studies":studies})

    if keyword_Geo:
        studies = Study.objects.filter(geo_accession__contains=keyword_Geo)
        return render(request,"StudySearch.html",{"studies":studies}) 
  

    studies = Study.objects.all()
    return render(request,"StudySearch.html",{"studies":studies})

def StudySearchPage(request,id):
    studies1 = Study.objects.filter(id=id).first()
    studies = Study.objects.filter(id=id).all()
    experiments = studies1.experiment.all()
    
    return render(request,"StudySearchPage.html",{"studies":studies,"experiments":experiments})


  



