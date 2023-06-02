from django.contrib import admin
from .models import Question, Answer, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'username', 'correct_answer')
    inlines = [ChoiceInline]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'username', 'question')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)