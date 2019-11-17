from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic

# https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-display/#generic-views-of-objects

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    # https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-display/#making-friendly-template-contexts

    # https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-display/#dynamic-filtering
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


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
