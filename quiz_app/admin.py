from django.contrib import admin
from . import models

#!------------- TabularInline Usage  ----------------------
class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right',
    ]
class QuizInlineModel(admin.TabularInline):
    model = models.Quiz
    fields = [
        'title',
    ]
class QuestionInlineModel(admin.TabularInline):
    model = models.Question
    fields = [
        'title',
        'difficulty',
    ]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    inlines = [
        QuizInlineModel,
    ]
    list_filter = ("name",)
    search_fields = ("name",)
@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'category'
    ]
    inlines = [
        QuestionInlineModel,
    ]
    list_filter = ("title",)
    search_fields = ("title",)
@admin.register(models.Question)    
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
        'difficulty',
    ]
    list_display = [
        'title',
        'quiz',
        'difficulty',
        'updatedDate'
    ]
    inlines = [
        AnswerInlineModel,
    ]
    list_filter = ('quiz', 'difficulty', 'updatedDate')
    search_fields = ("title",)
    
@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question',
        'updatedDate'
    ]
    list_filter = ('answer_text', 'is_right', 'updatedDate')
    search_fields = ('answer_text',)