from rest_framework.serializers import ModelSerializer
from .models import Subject, Test, Question, Choice

class SubjectsSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TestsSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class AnswerSerializerAll(ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'      