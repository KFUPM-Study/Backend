from django.db import models
from django.contrib.auth.models import User

    

class Subject(models.Model):
    title = models.CharField(max_length= 24, primary_key=True)
    picture = models.ImageField(upload_to=r"frontend/static/media/subject_pic")

    def __str__(self):
        return f'{self.title}'

class Test(models.Model):
    title = models.CharField(max_length= 24, blank= True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
    def getHighScore(self):
        return self.questions.count()

    
class Question(models.Model):
    questionBody = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")

    def getCorrectAnswer(self):
        return self.choices.filter(isCorrect = True)

    def __str__(self):
        return f'{self.questionBody}'

class Choice(models.Model):
    choice_body = models.TextField()
    isCorrect = models.BooleanField()
    question = models.ForeignKey(Question,on_delete=models.CASCADE, related_name="choices")
    

    def __str__(self):
        return f'{self.choice_body}'
    
class TakeTest(models.Model):
    # Tests history for users
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tests")
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def getScore(self):
        # return the number of correct answers
        return self.answeredQuestions.filter(answer__isCorrect = True).count()

    def __str__(self):
        return f'({self.user.username}){self.test.title} : {self.getScore()}'
    
class TakeQuestion(models.Model):
    # questions answered by user
    takeTest = models.ForeignKey(TakeTest, on_delete=models.CASCADE, related_name="answeredQuestions")
    answer = models.ForeignKey(Choice,on_delete=models.CASCADE)

    def getQuestion(self):
        return self.answer.question
    
    def __str__(self):
        return f"{self.getQuestion().questionBody}: {self.answer.isCorrect}"