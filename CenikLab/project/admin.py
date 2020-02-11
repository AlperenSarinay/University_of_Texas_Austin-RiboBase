from django.contrib import admin

from .models import Study
from .models import Srr
from .models import Experiment

# Register your models here.


admin.site.register(Study)
admin.site.register(Srr)
admin.site.register(Experiment)
