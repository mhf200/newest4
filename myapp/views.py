from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question, Answer, Translation
from translate import Translator


@csrf_exempt
def get_question(request):
    if request.method == 'GET':
        language = request.GET.get('language')

        question = Question.objects.order_by('?').first()

        # Check if translation for the given language exists in the Translation model
        translation = Translation.objects.filter(question=question, language=language).first()

        # If translation doesn't exist, perform translation and create a new Translation object
        if not translation:
            translator = Translator(to_lang=language)
            translated_question = translator.translate(question.question_text)
            translated_choices = [translator.translate(choice) for choice in question.choices.all().values_list('choice_text', flat=True)]
            translated_correct_answer = translator.translate(question.correct_answer)

            # Create a new Translation object
            translation = Translation(
                question=question,
                translated_question_text=translated_question,
                translated_choices=','.join(translated_choices),
                translated_correct_answer=translated_correct_answer,
                language=language
            )
            translation.save()

        response = {
            'question_id': question.id,
            'question_text': translation.translated_question_text,
            'answer_choices': translation.translated_choices.split(','),
            'username': question.username,
            'correct_answer': translation.translated_correct_answer
        }
        return JsonResponse(response)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
@csrf_exempt
def answer_question(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        username = request.POST.get('username')
        answer_text = request.POST.get('answer_text')

        if question_id and username and answer_text:
            try:
                question = Question.objects.get(id=question_id)
                answer = Answer(question=question, answer_text=answer_text, username=username)
                answer.save()

                if answer_text == question.correct_answer:
                    return JsonResponse({'success': 'Answer is correct!'})
                else:
                    return JsonResponse({'error': 'Answer is incorrect.'}, status=400)

            except Question.DoesNotExist:
                return JsonResponse({'error': 'Question does not exist.'}, status=400)