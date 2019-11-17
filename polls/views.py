from django.shortcuts import render
from django.http import HttpResponse, Http404

# from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))

    # REFACTORED: https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/#module-django.shortcuts
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist!")
    # return HttpResponse(f"Checking for question: {question_id}.")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "Looking at results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"+1 vote on question {question_id}.")
