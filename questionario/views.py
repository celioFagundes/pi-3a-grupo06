from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from usuario.forms import CustomUserCreationForm
from django.core.exceptions import PermissionDenied
from perguntas.models import Pergunta
from questionario.models import Questionario
from respostas.models import Resposta
from .forms import ResponderQuestionarioForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def answer_questionnaire_view(request):
    nome = None
    perguntas = Pergunta.objects.all().order_by('id')

    if request.user.is_authenticated:
        nome = request.user.nome
    if request.method == 'POST':
        form = ResponderQuestionarioForm(request.POST, perguntas=perguntas)
        if form.is_valid():
            respostas = form.cleaned_data
            pontuacao = sum(1 for resposta in respostas.values() if resposta == 'True')
            if pontuacao == 0:
                classificacao = 'SEM_SOFRIMENTO'
            elif 1 <= pontuacao <= 7:
                classificacao = 'LEVE'
            elif 8 <= pontuacao <= 14:
                classificacao = 'MODERADO'
            else:
                classificacao = 'GRAVE'

            questionario = Questionario.objects.create(
                usuario=request.user,
                data_resposta=timezone.now().date(),
                pontuacao=pontuacao,
                classificacao=classificacao
            )
            for pergunta in perguntas:
                resposta_valor = respostas.get(f'pergunta_{pergunta.id}') == 'True'
                Resposta.objects.create(
                    questionario=questionario,
                    pergunta=pergunta,
                    resposta=resposta_valor
                )

            return redirect('resultado-questionario', questionario_id=questionario.id)

    else:
        form = ResponderQuestionarioForm(perguntas=perguntas)

    return render(request, 'questionario.html', {'form': form, 'nome':nome})

@login_required
def results_questionnaire_view(request,questionario_id):
    nome = None
    questionario = Questionario.objects.get(id=questionario_id)
    if request.user.is_authenticated:
        nome = request.user.nome
    return render(request, 'questionario-resultado.html', {'nome':nome,'questionario': questionario,})

