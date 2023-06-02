import uuid
from django.db import models


class Question(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    question_text = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices' , null=True)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=200)

    def __str__(self):
        return str(self.answer_text)


class Translation(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='translations')
    translated_question_text = models.CharField(max_length=200)
    translated_choices = models.CharField(max_length=1000)
    translated_correct_answer = models.UUIDField(default=uuid.uuid4, editable=False)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.translated_question_text