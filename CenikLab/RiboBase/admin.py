from django.contrib import admin

from .models import Study
from .models import MetaData
from .models import Experiment_show
#from .models import DataShow

# Register your models here.

admin.site.register(Study)

admin.site.register(MetaData)
admin.site.register(Experiment_show)
#admin.site.register(DataShow)
