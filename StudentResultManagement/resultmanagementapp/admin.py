from django.contrib import admin
from resultmanagementapp.models import SixResultModel, SevenResultModel, EightResultModel, FacultyModel, CoursesModel

# Register your models here.
class SixResult(admin.ModelAdmin):
    list_display = ('username', 'name', 'english', 'maths', 'science')

class SevenResult(admin.ModelAdmin):
    list_display = ('username', 'name', 'english', 'maths', 'science')

class EightResult(admin.ModelAdmin):
    list_display = ('username', 'name', 'english', 'maths', 'science')

class Faculty_admin(admin.ModelAdmin):
     list_display = ("name", "image", "qualifications", "introduction")

class Courses_admin(admin.ModelAdmin):
     list_display = ("image", "title", "introduction")


admin.site.register(SixResultModel, SixResult)
admin.site.register(SevenResultModel, SevenResult)
admin.site.register(EightResultModel, EightResult)
admin.site.register(FacultyModel, Faculty_admin)
admin.site.register(CoursesModel, Courses_admin)