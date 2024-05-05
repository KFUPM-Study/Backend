from django.contrib import admin
from .models import Subject, Test, History, SolvedQuestion,Question, Choice

# Register your models here.
admin.site.register(Subject)
admin.site.register(Test)
admin.site.register(History)
admin.site.register(SolvedQuestion)
admin.site.register(Question)
admin.site.register(Choice)