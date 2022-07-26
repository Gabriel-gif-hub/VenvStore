from tkinter import E
from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Departamento
# Create your views here.

def index(request):
    meu_nome = 'Neymar Jr'
    gênero = 'm'
    context = {'nome': meu_nome, 'artigo': 'o' if gênero == 'm' else 'a'}
    return render(request, 'index.html', context)

def teste(request):
    depto = Departamento.objects.all()
    context = {'departamentos': depto}
    return render(request, 'teste.html', context)
