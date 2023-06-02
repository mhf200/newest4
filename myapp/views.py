import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question, Answer, Translation
from translate import Translator



@csrf_exempt
def get_question(request):
    if request.method == 'GET':
        language = request.GET.get('language')

        question = Question.objects.order_by('?').first()


        translation = Translation.objects.filter(question=question, language=language).first()


        if not translation:
            translator = Translator(to_lang=language)
            translated_question = translator.translate(question.question_text)
            translated_choices = [translator.translate(choice.choice_text) for choice in question.choices.all()]
            translated_correct_answer = str(uuid.uuid4())
            translation = Translation(
                question=question,
                translated_question_text=translated_question,
                translated_choices=','.join(translated_choices),
                translated_correct_answer=translated_correct_answer,
                language=language
            )
            translation.save()

        response = {
            'question_uuid': str(question.uuid),
            'question_text': translation.translated_question_text,
            'answer_choices': translation.translated_choices.split(','),
            'username': question.username,
            'correct_answer': str(translation.translated_correct_answer)
        }
        return JsonResponse(response)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def answer_question(request):
    if request.method == 'POST':
        question_uuid = request.POST.get('question_uuid')
        username = request.POST.get('username')
        answer_text = request.POST.get('answer_text')

        if question_uuid and username and answer_text:
            try:
                question = Question.objects.get(uuid=question_uuid)
                answer = Answer(question=question, answer_text=answer_text, username=username)
                answer.save()

                if answer_text == str(question.correct_answer):
                    return JsonResponse({'success': 'Answer is correct!'})
                else:
                    return JsonResponse({'error': 'Answer is incorrect.'}, status=400)

            except Question.DoesNotExist:
                return JsonResponse({'error': 'Question does not exist.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)

