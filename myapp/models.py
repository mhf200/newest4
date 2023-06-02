from django.db import models


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices' , null=True)
    choice_text = models.CharField(max_length=200)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

class Translation(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='translations')
    translated_question_text = models.CharField(max_length=200)
    translated_choices = models.CharField(max_length=1000)
    translated_correct_answer = models.CharField(max_length=200)
    language = models.CharField(max_length=50)