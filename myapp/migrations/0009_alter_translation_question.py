# Generated by Django 4.0 on 2023-06-02 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_answer_answer_text_alter_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='myapp.question'),
        ),
    ]
