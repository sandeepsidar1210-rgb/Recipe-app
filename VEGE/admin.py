from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Receipe)


admin.site.register(Student)
admin.site.register(Department)
admin.site.register(studentID)


class SubjectMarksAdmin(admin.ModelAdmin):
    list_display=['student', 'subject', 'marks']

admin.site.register(Subject )
admin.site.register(StudentMarks , SubjectMarksAdmin)
