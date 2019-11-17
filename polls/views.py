from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World. Polls=Index.")


def detail(request, question_id):
    return HttpResponse(f"Checking for question: {question_id}.")


def results(request, question_id):
    response = "Looking at results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"+1 vote on question {question_id}.")
