from django.contrib import admin
from newsApp.models import Students


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

admin.site.register(Students,StudentAdmin)
