from django.contrib import admin
from .models import Subject, Test, TakeTest, TakeQuestion,CustomUser,Question, Choice

# Register your models here.
admin.site.register(Subject)
admin.site.register(Test)
admin.site.register(TakeTest)
admin.site.register(TakeQuestion)
admin.site.register(CustomUser)
admin.site.register(Question)
admin.site.register(Choice)