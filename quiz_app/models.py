from django.db import models
from django.utils.translation import gettext_lazy as t


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name=t('Category Name'))
     
    def __str__ (self):
        return self.name
    
    class Meta:
        verbose_name = t('Category')
        verbose_name_plural = t('Categories')
        ordering = ['name']
    
class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, verbose_name=t('Title'))
    createdDate = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.title
    
    class Meta:
        verbose_name = t('Quiz')
        verbose_name_plural = t('Quizzes')
        ordering = ['id']

class Updated(models.Model):
    updatedDate = models.DateTimeField(auto_now=True, verbose_name=t('Last Updated')) 

    class Meta:
        abstract = True

class Question(Updated):
    scale = [
        ('Starter', 'Starter'),
        ('Elementary', 'Elementary'),
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert')
    ]
 
    quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=t('Title'))
    difficulty = models.CharField(max_length=255,choices=scale)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=t('Date Created'))
    
    def __str__ (self):
        return self.title
    class Meta:
        verbose_name = t('Question')
        verbose_name_plural = t('Question')
        ordering = ['title']
    
class Answer(Updated):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, verbose_name=t('Answer Text'))
    is_right = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = t('Answer')
        verbose_name_plural = t('Answers')
        ordering = ['id']
    
    