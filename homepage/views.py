from django.shortcuts import render


def homepage(request):
    nome = None
    if request.user.is_authenticated:
        nome = request.user.nome
    context = {'nome': nome}
    return render(request, 'homepage.html', context)
