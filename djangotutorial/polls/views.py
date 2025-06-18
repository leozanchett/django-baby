from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from polls.models import Question, Choice
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {"latest_question_list": latest_question_list}
#     return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

# def detail(request, question_id):
#     try:
#         # Tenta obter a questão com o ID fornecido
#         question = Question.objects.get(id=question_id)
#     except Question.DoesNotExist:
#         # Se a questão não for encontrada, retorna uma resposta 404
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) # O 'choice_set' é um related manager que permite acessar as escolhas associadas a uma questão.
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1 # O F() é usado para referenciar o campo 'votes' diretamente no banco de dados, evitando a necessidade de carregar o objeto Choice inteiro na memória.
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))