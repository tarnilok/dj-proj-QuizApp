from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import pagination
from rest_framework.serializers import Serializer
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Question, Answer, Category, Quiz
from .serializers import CategorySerializer, QuizSerializer, QuestionSerializer
from .permissions import IsUserOrNotAllowed
from .pagination import NewPageNumberPagination

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
class QuizList(ListAPIView): 
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get(self, request, format=None, **kwargs):
        category_name = Quiz.objects.filter(category__name=kwargs['category'])
        serializer = QuizSerializer(category_name, many=True)
        return Response(serializer.data)

class QuestionList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = NewPageNumberPagination
    
    def get(self, request, format=None, **kwargs):
        quiz_name = Question.objects.filter(quiz__title=kwargs['title'])
        page = self.paginate_queryset(quiz_name)
        serializer = QuestionSerializer(page, many=True)                                           
        return self.get_paginated_response(serializer.data)