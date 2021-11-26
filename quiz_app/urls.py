from django.urls import path, include
from .views import RegisterApi, CategoryList, QuizList, QuestionList

urlpatterns = [
    path('auth_login/', include('dj_rest_auth.urls')),
    # path('auth_register/', include('dj_rest_auth.registration.urls')),
    path('register/', RegisterApi.as_view()),
    path('quiz/', CategoryList.as_view()),
    path('quiz/<str:category>', QuizList.as_view()),
    path('quiz/<str:category>/<str:title>', QuestionList.as_view()),
]