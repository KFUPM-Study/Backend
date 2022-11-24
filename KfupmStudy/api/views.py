from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import SubjectsSerializer, TestsSerializer, AnswerSerializer,QuestionSerializer, TestSerializer
from .models import Subject, Test, Question, Answer

# Create your views here.

@api_view(['GET'])
def getSubjects(request):
    subjects = Subject.objects.all()
    serializer = SubjectsSerializer(subjects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTests(request, subject):
    subject = Subject.objects.get(name = subject)
    test = Test.objects.filter(subject = subject)
    serializer = TestsSerializer(test, many = True)
    for test in serializer.data:
        test['picture'] = str(subject.picture)
    return Response(serializer.data)

class TakeTest(APIView):
    def get(self, request, test):
        test = Test.objects.get(title = test)
        Tserializer = TestSerializer(test)
        data = Tserializer.data

        questions = {}
        for question in data['questions']:
            q = Question.objects.get(id = question)
            serializer = QuestionSerializer(q)

            answers = {}
            num_answer = 0
            for answer in serializer.data['answers']:
                a = Answer.objects.get(id = answer)
                answer_serializer = AnswerSerializer(a)
                answers[num_answer] = answer_serializer.data 
                num_answer += 1
            questions[q.question_body] = answers
            
               
        data["questions"] = questions    


        return Response(data)
    def post(self, request):
        pass