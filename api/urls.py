from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.getSubjects, name='subjects-api'),
    path('subjects/<str:subject>', views.getTests, name='tests-api'),
    path('tests/<int:id>', views.getTest, name='GetTest-api')
    #,path('takeTest/', views.TakeTest.as_view(), name = 'TakeTest-api')
]


