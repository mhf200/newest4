# Generated by Django 4.0 on 2023-06-02 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_question_choices_choice_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translated_question_text', models.CharField(max_length=200)),
                ('translated_choices', models.CharField(max_length=1000)),
                ('translated_correct_answer', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=50)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='translation', to='myapp.question')),
            ],
        ),
    ]
