from django.shortcuts import render
from django.http import HttpResponse
import django.db

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"Checking for question: {question_id}.")


def results(request, question_id):
    response = "Looking at results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"+1 vote on question {question_id}.")
