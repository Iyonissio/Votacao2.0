from django.shortcuts import redirect, render
from polls.models import Eleitor


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
