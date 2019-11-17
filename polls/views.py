from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))

    # REFACTORED: https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/#module-django.shortcuts
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # V1: return HttpResponse(f"Checking for question: {question_id}.")

    # V2: try:
    # V2:     question = Question.objects.get(pk=question_id)
    # V2: except Question.DoesNotExist:
    # V2:     raise Http404("Question does not exist!")
    # V2: return render(request, "polls/detail.html", {"question": question})

    # V3:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "Looking at results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    # return HttpResponse(f"+1 vote on question {question_id}.")

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "Choice not selected!",},
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # TODO: IMPORTANT ==>
        # Always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
