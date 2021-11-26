from django.contrib import admin
from .models import Quiz, Answer, Category, Question
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline 

# #!------------- TabularInline Usage  ----------------------
# class AnswerInlineModel(admin.TabularInline):
#     model = Answer
#     fields = [
#         'answer_text',
#         'is_right',
#     ]
# class QuizInlineModel(admin.TabularInline):
#     model = Quiz
#     fields = [
#         'title',
#     ]
# class QuestionInlineModel(admin.TabularInline):
#     model = Question
#     fields = [
#         'title',
#         'difficulty',
#     ]

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = [
#         'name',
#     ]
#     inlines = [
#         QuizInlineModel,
#     ]
#     list_filter = ("name",)
#     search_fields = ("name",)
# @admin.register(Quiz)
# class QuizAdmin(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'title',
#         'category'
#     ]
#     inlines = [
#         QuestionInlineModel,
#     ]
#     list_filter = ("title",)
#     search_fields = ("title",)
# @admin.register(Question)    
# class QuestionAdmin(admin.ModelAdmin):
#     fields = [
#         'title',
#         'quiz',
#         'difficulty',
#     ]
#     list_display = [
#         'title',
#         'quiz',
#         'difficulty',
#         'updatedDate'
#     ]
#     inlines = [
#         AnswerInlineModel,
#     ]
#     list_filter = ('quiz', 'difficulty', 'updatedDate')
#     search_fields = ("title",)
# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = [
#         'answer_text',
#         'is_right',
#         'question',
#         'updatedDate'
#     ]
#     list_filter = ('answer_text', 'is_right', 'updatedDate')
#     search_fields = ('answer_text',)
    
#! --------------- Django Nested Admin --------------------

class TableOfAnswerAdmin(NestedTabularInline):
    model = Answer
    extra = 4
class TableOfQuestionAdmin(NestedTabularInline):
    model = Question
    extra = 1
    inlines = [TableOfAnswerAdmin]
class TableOfCategoryAdmin(NestedTabularInline):
    model = Category
class TableOfQuizAdmin(NestedModelAdmin):
    list_display = [
        'id',
        'title',
        'category'
    ]
    inlines = [TableOfQuestionAdmin]
    list_filter = ("title",)
    search_fields = ("title",) 
admin.site.register(Quiz, TableOfQuizAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    list_filter = ("name",)
    search_fields = ("name",)
admin.site.register(Category, CategoryAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'quiz',
        'difficulty',
        'updatedDate'
    ]
    list_filter = ('quiz', 'difficulty', 'updatedDate')
    search_fields = ("title",)
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question',
        'updatedDate'
    ]
    list_filter = ('is_right', 'updatedDate')
    search_fields = ('answer_text',)
admin.site.register(Answer, AnswerAdmin)

    



