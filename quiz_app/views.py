from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Question, Answer, Category, Quiz
from .serializers import CategorySerializer, QuizSerializer, QuestionSerializer
from .permissions import IsUserOrNotAllowed

#!Auth views
class RegisterApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message":"User successfully created."
        })
        
#! Drf view
class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsUserOrNotAllowed]
class QuizList(APIView): 
    def get(self, request, format=None, **kwargs):
        category_name = Quiz.objects.filter(category__name=kwargs['category'])
        serializer = QuizSerializer(category_name, many=True)
        return Response(serializer.data)


class QuestionList(APIView):
    def get(self, request, format=None, **kwargs):
        quiz_name = Question.objects.filter(quiz__title=kwargs['title'])
        serializer = QuestionSerializer(quiz_name, many=True)
        return Response(serializer.data)