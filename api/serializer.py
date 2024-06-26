from rest_framework.serializers import ModelSerializer, ImageField, IntegerField
from .models import Subject, Test, Question, Choice

class SubjectsSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ["title", "picture"]

class TestsSerializer(ModelSerializer):
    picture = ImageField(source="subject.picture")
    class Meta:
        model = Test
        fields = ["id", "title", "picture"]

class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", 'choiceBody']
class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many = True)
    class Meta:
        model = Question
        fields = ["id", "questionBody", "choices"]

class TestSerializer(ModelSerializer):
    questions = QuestionSerializer(many = True)
    class Meta:
        model = Test
        fields = ["id", "title", "questions", "num"]
        #depth = 2


class AnswerSerializerAll(ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'      