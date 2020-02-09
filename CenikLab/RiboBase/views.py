from django.shortcuts import render,redirect,get_object_or_404
from .models import Experiment_show,MetaData,Study
from .forms import AddExperimentForm,AddDataForm
from django.contrib import messages

# Create your views here.

def index(request):
    studies = Study.objects.all()
    experiments = Experiment_show.objects.all()
    return render(request,"index.html",{"experiments":experiments,"studies":studies})

def about(request):
    return render(request,"about.html")

def DataSearch(request):

    keyword_Species = request.GET.get("keyword_species")
    keyword_cell_tissue = request.GET.get("keyword_Cell_tissue")
    keyword_Cell_line = request.GET.get("keyword_cell_line")
    keyword_dataset = request.GET.get("keyword_Dataset")
    keyword_instrument = request.GET.get("keyword_Instrument")
    keyword_sra = request.GET.get("keyword_SRA")
    keyword_geo = request.GET.get("keyword_Geo")

    if keyword_Species:
        experiments = Experiment_show.objects.filter(species__contains=keyword_Species)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_cell_tissue:
        experiments = Experiment_show.objects.filter(Cell_Tissue__contains=keyword_cell_tissue)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_Cell_line:
        experiments = Experiment_show.objects.filter(cellLine_Strain__contains=keyword_Cell_line)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_dataset:
        experiments = Experiment_show.objects.filter(Dataset_Type__contains=keyword_dataset)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_instrument:
        experiments = Experiment_show.objects.filter(Instrument__contains=keyword_instrument)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_sra:
        experiments = Experiment_show.objects.filter(SRA_Accession__contains=keyword_sra)
        return render(request,"DataSearch.html",{"experiments":experiments}) 
        
    if keyword_geo:
        experiments = Experiment_show.objects.filter(Geo__contains=keyword_geo)
        return render(request,"DataSearch.html",{"experiments":experiments})   

    experiments = Experiment_show.objects.all()
    return render(request,"DataSearch.html",{"experiments":experiments})

def DataDowload(request):

    keyword_Species = request.GET.get("keyword_species")
    keyword_cell_tissue = request.GET.get("keyword_Cell_tissue")
    keyword_Cell_line = request.GET.get("keyword_cell_line")
    keyword_dataset = request.GET.get("keyword_Dataset")
    keyword_instrument = request.GET.get("keyword_Instrument")
    keyword_sra = request.GET.get("keyword_SRA")
    keyword_geo = request.GET.get("keyword_Geo")

    if keyword_Species:
        experiments = Experiment_show.objects.filter(species__contains=keyword_Species)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_cell_tissue:
        experiments = Experiment_show.objects.filter(Cell_Tissue__contains=keyword_cell_tissue)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_Cell_line:
        experiments = Experiment_show.objects.filter(cellLine_Strain__contains=keyword_Cell_line)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_dataset:
        experiments = Experiment_show.objects.filter(Dataset_Type__contains=keyword_dataset)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_instrument:
        experiments = Experiment_show.objects.filter(Instrument__contains=keyword_instrument)
        return render(request,"DataSearch.html",{"experiments":experiments})

    if keyword_sra:
        experiments = Experiment_show.objects.filter(SRA_Accession__contains=keyword_sra)
        return render(request,"DataSearch.html",{"experiments":experiments}) 
        
    if keyword_geo:
        experiments = Experiment_show.objects.filter(Geo__contains=keyword_geo)
        return render(request,"DataSearch.html",{"experiments":experiments})  
    
    experiments = Experiment_show.objects.all()
    return render(request,"DataDowload.html",{"experiments":experiments})

def AddExperiment(request):

    form = AddExperimentForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,"The Experiment was successfully created.")
        return redirect("AddExperiment")
        
    return render(request,"AddExperiment.html",{"form":form})

def addData(request):
    form = AddDataForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,"the MetaData was successfully created.")
        return redirect("addData")

    return render(request,"addData.html",{"form":form})

def DataSearchPage(request,id):
    
    Experiment1 = Experiment_show.objects.filter(id=id).first()
    Metadata = Experiment1.metadata.all()
    experiments = Experiment_show.objects.filter(id=id).all()
    
    
    return render(request,"DataSearchPage.html",{"experiments":experiments,"Metadata":Metadata})

def Comparasion(request):

    keyword_Species = request.GET.get("keyword_species")
    keyword_cell_tissue = request.GET.get("keyword_Cell_tissue")
    keyword_Cell_line = request.GET.get("keyword_cell_line")
    keyword_dataset = request.GET.get("keyword_Dataset")
    keyword_instrument = request.GET.get("keyword_Instrument")
    keyword_sra = request.GET.get("keyword_SRA")
    keyword_geo = request.GET.get("keyword_Geo")

    if keyword_Species:
        experiments = Experiment_show.objects.filter(species__contains=keyword_Species)
        return render(request,"Comparasion.html",{"experiments":experiments})

    if keyword_cell_tissue:
        experiments = Experiment_show.objects.filter(Cell_Tissue__contains=keyword_cell_tissue)
        return render(request,"Comparasion.html",{"experiments":experiments})

    if keyword_Cell_line:
        experiments = Experiment_show.objects.filter(cellLine_Strain__contains=keyword_Cell_line)
        return render(request,"Comparasion.html",{"experiments":experiments})

    if keyword_dataset:
        experiments = Experiment_show.objects.filter(Dataset_Type__contains=keyword_dataset)
        return render(request,"Comparasion.html",{"experiments":experiments})

    if keyword_instrument:
        experiments = Experiment_show.objects.filter(Instrument__contains=keyword_instrument)
        return render(request,"Comparasion.html",{"experiments":experiments})

    if keyword_sra:
        experiments = Experiment_show.objects.filter(SRA_Accession__contains=keyword_sra)
        return render(request,"Comparasion.html",{"experiments":experiments}) 
        
    if keyword_geo:
        experiments = Experiment_show.objects.filter(Geo__contains=keyword_geo)
        return render(request,"Comparasion.html",{"experiments":experiments})  
    
    experiments = Experiment_show.objects.all()
    return render(request,"Comparasion.html",{"experiments":experiments})
    
