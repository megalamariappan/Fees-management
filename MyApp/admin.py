from django.contrib import admin
from .models import Student,department,CourseLevel,Course,payment
# Register your models here.

admin.site.register(Student)
admin.site.register(department)
admin.site.register(CourseLevel)
admin.site.register(Course)
admin.site.register(payment)