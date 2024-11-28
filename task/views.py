from django.shortcuts import render, redirect
from .models import Tarefa
from django.shortcuts import render, redirect, get_object_or_404

def lista_tarefas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        if titulo:
            Tarefa.objects.create(titulo=titulo)
            return redirect('lista_tarefas')

    tarefas = Tarefa.objects.all()
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})

def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('lista_tarefas')


def concluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.concluida = True
    tarefa.save()
    return redirect('lista_tarefas')

