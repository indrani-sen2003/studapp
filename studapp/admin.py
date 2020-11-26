from django.contrib import admin
from studapp.models import major
from studapp.models import course
from studapp.models import student

# Register your models here.

class admin_major(admin.ModelAdmin):
    pass
admin.site.register(major,admin_major)
class admin_course(admin.ModelAdmin):
    pass
admin.site.register(course,admin_course)
class admin_stud(admin.ModelAdmin):
    pass
admin.site.register(student,admin_course)

