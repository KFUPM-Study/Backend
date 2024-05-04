from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('subjects/', views.getSubjects, name='subjects-api'),
    path('subjects/<str:subject>', views.getTests, name='tests-api'),
    path('tests/<int:id>', views.getTest, name='GetTest-api')
    #,path('takeTest/', views.TakeTest.as_view(), name = 'TakeTest-api')
]


