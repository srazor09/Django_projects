from django.contrib import admin
from testApp.models import ContactInfo1,Student1,Teacher1
from testApp.models import Parent1,Child1,SubChild

# Register your models here.



admin.site.register(ContactInfo1)
admin.site.register(Student1)
admin.site.register(Teacher1)

admin.site.register(Parent1)
admin.site.register(Child1)
admin.site.register(SubChild)


"""
class ContactInfo1Admin(model.ModelAdmin):
    list_display=['name','email','address']


class Student1Admin(model.ModelAdmin):
    list_display=['name','email','address','rollno',]


class Teacher1Admin(model.ModelAdmin)
"""
