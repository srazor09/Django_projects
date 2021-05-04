from django.contrib import admin
from testApp.models import filterModel

# Register your models here.

class FilterModelAdmin(admin.ModelAdmin):
    list_display=['name','subject','dept','date']


admin.site.register(filterModel,FilterModelAdmin)
