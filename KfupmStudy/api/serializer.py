from rest_framework.serializers import ModelSerializer
from .models import Subject, Test, Question, Answer

class SubjectsSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TestsSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = ['title']

class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = ['title', 'score', 'questions']

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_body']

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','choice_A', 'choice_B', 'choice_C', 'choice_D']