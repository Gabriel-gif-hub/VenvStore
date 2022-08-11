from multiprocessing import context
from tkinter import E
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Departamento, Categoria, Produto
from django.core.mail import send_mail


# Create your views here.

def index(request):
    meu_nome = 'Gabriel'
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
    depto = Departamento.objects.get(id = id)
    context = {'categorias': lista_categorias,
                'departamento': depto
    }
    return render(request, 'categorias.html', context)

def produtos(request, id):
    lista_produtos = Produto.objects.filter(categoria_id = id)
    depto = Departamento.objects.get(id = id)
    context = {'produtos': lista_produtos,
                'departamento': depto 
     }
    return render(request, 'produtos.html', context)

def produto_detalhe(request,id):
    produto = Produto.objects.get(id = id)
    context = {
        'produto':produto
       
    }

    return render(request, 'produto_detalhe.html', context)

def institucional(request):
    return render(request, 'institucional.html')

def contato(request):
    return render(request, 'contato.html')

def enviar_email(request):
    nome = request.POST['nome']
    telefone = request.POST['telefone']
    assunto = request.POST['assunto']
    mensagem = request.POST['mensagem']
    remetente = request.POST['email']
    destinatario = ['gabrieloliveira2505@gmail.com']
    corpo = f"Nome: {nome} \nTelefone: {telefone} \nMensagem: {mensagem}"
    try:
        send_mail(assunto, corpo, remetente, destinatario)
        context = {'msg': 'E-mail enviado com sucesso!'}
    except:
        context = {'msg': 'Erro ao enviar o e-mail!'}

    return render(request, 'contato.html',context)
