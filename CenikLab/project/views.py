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

    form = AddExperimentForm(request.POST or None)
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
        return redirect("UpdateExperiment")

    return render(request,"Update.html",{"form":form})

def AddSRR(request):

    form = AddSrrForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"The SRR  was successfully created.")
        return redirect("AddSRR")
        
    return render(request,"AddSRR.html",{"form":form})

def StudySearch(request):
    return render(request,"StudySearch.html")

def StudySearchPage(request):
    return render(request,"StudySearchPage.html")




