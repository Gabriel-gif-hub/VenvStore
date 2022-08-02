from tkinter import E
from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Departamento, Categoria, Produto


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

def departamentos(request):
    depto = Departamento.objects.all()
    context = {'departamentos': depto}
    return render(request, 'departamentos.html', context)

def categorias(request, id):
    lista_categorias = Categoria.objects.filter(departamento_id = id)
    context = {'categorias': lista_categorias}
    return render(request, 'categorias.html', context)

def produtos(request, id):
    lista_produtos = Produto.objects.filter(categoria_id = id)
    context = {'produtos': lista_produtos }
    return render(request, 'produtos.html', context)