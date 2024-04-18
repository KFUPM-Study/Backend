from django.contrib import admin
from .models import Subject, Test, Score,Student,Question, Choice

# Register your models here.
admin.site.register(Subject)
admin.site.register(Test)
admin.site.register(Score)
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Choice)