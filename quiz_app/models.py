from django.db import models
from django.utils.translation import gettext_lazy as t


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=t('Category Name'))
     
    def __str__ (self):
        return f"Quiz Category: {self.name}"
    
    class Meta:
        verbose_name = t('Category')
        verbose_name_plural = t('Categories')
        ordering = ['name']
    
class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=30, verbose_name=t('Title'))
    createdDate = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return f"Quiz Name: {self.title}"
    
    class Meta:
        verbose_name = t('Quiz')
        verbose_name_plural = t('Quizzes')
        ordering = ['title']

class Updated(models.Model):
    updatedDate = models.DateTimeField(auto_now=True, verbose_name=t('Last Updated')) 

    class Meta:
        abstract = True

class Question(Updated):
    scale = {
        (0, t('Starter')),
        (1, t('Elementary')),
        (2, t('Beginner')),
        (3, t('Intermediate')),
        (4, t('Advanced')),
        (5, t('Expert'))
    }
 
    quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=30, verbose_name=t('Title'))
    difficulty = models.IntegerField(choices=scale, verbose_name=t('Difficulty'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=t('Date Created'))
    
    def __str__ (self):
        return {self.title}
    class Meta:
        verbose_name = t('Question')
        verbose_name_plural = t('Question')
        ordering = ['title']
    
class Answer(Updated):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=t('Answer Text'))
    is_right = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = t('Answer')
        verbose_name_plural = t('Answers')
        ordering = ['id']
    
