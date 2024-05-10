from django.contrib import admin
from .models import Subject, Test, TestAttempt, QuestionAttempt,Question, Choice

# Register your models here.
admin.site.register(Subject)
admin.site.register(Test)
admin.site.register(TestAttempt)
admin.site.register(QuestionAttempt)
admin.site.register(Question)
admin.site.register(Choice)