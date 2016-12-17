from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response

from .models import Question
from .models import signals

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'stockscreener/index.html', context)

#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'stockscreener/detail.html', {'question': question})

def index(request):
	signalss = signals.objects.distinct('BBG').order_by('BBG')
	return render_to_response('home.html', {'signals': signalss})

