from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.getSubjects, name='subjects-api'),
    path('subjects/<str:subject>', views.getTests, name='tests-api'),
    path('tests/<str:test>', views.TakeTest.as_view(), name='takeTest-api')
]


