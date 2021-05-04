from django.contrib import admin
from jobsApp.models import hydjobs,bangljobs,chennjobs,punejobs

# register your models here.

class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class bangljobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class chennjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(bangljobs,bangljobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
admin.site.register(chennjobs,chennjobsAdmin)
