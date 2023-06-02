from django.contrib import admin
from .models import Question, Answer, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'username', 'correct_answer')
    inlines = [ChoiceInline]
    readonly_fields = ('id',)  # Make the UUID field read-only


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'username', 'question')
    readonly_fields = ('id',)  # Make the UUID field read-only


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
