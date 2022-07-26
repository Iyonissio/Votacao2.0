from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice, Eleitor
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

# Get questions and display them
# @login_required
from django.shortcuts import redirect, render


def index(request):
    eleitores = Eleitor.objects.all()

    context = {
        'eleitores': eleitores,
    }
    return render(request, 'index.html', context)


def edit(request):
    eleitores = Eleitor.objects.all()

    context = {
        'eleitores': eleitores,
    }

    return redirect(request, 'index.html', context)


def update(request, codigo):
    if request.method == "POST":
        estado = request.POST.get("estado")
        bilhete_de_identidade = request.POST.get("bilhete_de_identidade")
        sexo = request.POST.get("sexo")
        nome = request.POST.get("nome")

        emp = Eleitor(
            codigo=codigo,
            estado=estado,
            bilhete_de_identidade=bilhete_de_identidade,
            sexo=sexo,
            nome=nome,
        )

        emp.save()
        return redirect('home')

    return redirect(request, 'index.html')


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# Show specific question and choices
@login_required
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', { 'question': question })

# Get question and display results
# @login_required
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', { 'question': question })

# Vote for a question choice
@login_required
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

@login_required
def resultsData(request, obj):
    votedata = []

    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()

    for i in votes:
        votedata.append({i.choice_text:i.votes})

    return JsonResponse(votedata, safe=False)
