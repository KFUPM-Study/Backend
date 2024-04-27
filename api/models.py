from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    tests = models.ManyToManyField("Score", related_name="student")
    

class Subject(models.Model):
    name = models.CharField(max_length= 24)
    picture = models.ImageField(upload_to=r"frontend/static/media/subject_pic")

    def __str__(self):
        return f'{self.name}'

class Score(models.Model):
    test = models.ForeignKey('Test', on_delete=models.CASCADE, related_name='+')
    user_score = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.test.title} : {self.user_score}'

class Test(models.Model):
    title = models.CharField(max_length= 24, blank= True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    questions = models.ManyToManyField("Question")

    def __str__(self):
        return f'{self.title}'
    
    def getHighScore(self):
        return self.questions.count()

    
class Question(models.Model):
    question_body = models.TextField()
    choices = models.ManyToManyField("Choice")

    def getCorrectAnswer(self):
        return self.choices.filter(isCorrect = True)

    def __str__(self):
        return f'{self.question_body}'

class Choice(models.Model):
    choice_body = models.TextField()
    isCorrect = models.BooleanField()
    

    def __str__(self):
        return f'{self.choice_body}'