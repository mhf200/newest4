from django.contrib import admin
from .models import Question, Answer, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'username', 'display_correct_answer')
    inlines = [ChoiceInline]
    readonly_fields = ('display_correct_answer',)

    def display_correct_answer(self, obj):
        return str(obj.correct_answer)

    display_correct_answer.short_description = 'Correct Answer'


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'username', 'question')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)