from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    pass

class Subject(models.Model):
    name = models.CharField(max_length= 24)
    picture = models.ImageField(upload_to=r"frontend/static/media/subject_pic")

    def __str__(self):
        return f'{self.name}'

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey('Test', on_delete=models.CASCADE, related_name='+')
    user_score = models.PositiveIntegerField()
    

    def __str__(self):
        return f'{self.student.username}:{self.test.title} : {self.user_score}'

class Test(models.Model):
    title = models.CharField(max_length= 24, blank= True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null = True)
    score = models.PositiveIntegerField()
    questions = models.ManyToManyField("Question")
    def __str__(self):
        return f'{self.title}'
    
class Question(models.Model):
    question_body = models.TextField()
    question_num = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.question_num}.{self.question_body}'

class Answer(models.Model):
    choices = {
        ('A' , "A"),
        ('B' , "B"),
        ('C' , "C"),
        ('D' , "D"),
    }

    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

    choice_A = models.CharField(max_length=300, null=True, blank=True)
    choice_B = models.CharField(max_length=300, null=True, blank=True)
    choice_C = models.CharField(max_length=300, null=True, blank=True)
    choice_D = models.CharField(max_length=300, null=True, blank=True)
    correct_answer = models.CharField(choices=choices, max_length=1, null=True) 
    

    def __str__(self):
        return f'{self.question.question_body}'