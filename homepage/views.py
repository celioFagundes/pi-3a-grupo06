from django.shortcuts import render
from questionario.models import Questionario
from django.db.models import Count

def homepage(request):
    nome = None
    usuario = request.user

    classificacoes = {
        'SEM_SOFRIMENTO': 0,
        'LEVE': 0,
        'MODERADO': 0,
        'GRAVE': 0,
    }
    classificacoes_geral = { 
        'SEM_SOFRIMENTO': 0,
        'LEVE': 0,
        'MODERADO': 0,
        'GRAVE': 0,
    }
    questionarios = []

    if request.user.is_authenticated:
        nome = request.user.nome

        contagem_classificacao = (
            Questionario.objects.filter(usuario=usuario)
            .values('classificacao')
            .annotate(total=Count('id'))
        )

        for item in contagem_classificacao:
            classificacoes[item['classificacao']] = item['total']

        if request.user.is_superuser:
            contagem_classificacao_geral = (
                Questionario.objects.values('classificacao')
                .annotate(total=Count('id'))
            )

            for item in contagem_classificacao_geral:
                classificacoes_geral[item['classificacao']] = item['total']

            questionarios = Questionario.objects.all().order_by('-data_resposta')

        else:
            questionarios = Questionario.objects.filter(usuario=usuario).order_by('-data_resposta')

    return render(request, 'homepage.html', {
        'nome': nome,
        'classificacoes': classificacoes, 
        'classificacoes_geral': classificacoes_geral,
        'questionarios': questionarios
    })
