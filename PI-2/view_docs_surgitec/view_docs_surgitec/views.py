from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Funcionario
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'home.html') 


def cadastrar_funcionario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        usuario = request.POST['usuario']
        senha = make_password(request.POST['senha'])
        funcao = request.POST['funcao'].upper()
        
        # Cria o usuário do Django
        user = User.objects.create(username=usuario, password=senha)

        # Cria o funcionário associado
        Funcionario.objects.create(nome=nome, usuario=user, funcao=funcao)

        # Redireciona para a página de sucesso
        return redirect('cadastrar_funcionario_sucesso')  

    return render(request, 'cadastrar_funcionario.html')

def cadastro_sucesso(request):
    return render(request, 'cadastro_sucesso.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Verifica se o usuário existe
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Faz login no sistema
            login(request, user)  


            # Verifica a função do funcionário
            funcionario = Funcionario.objects.get(usuario=user)
            if funcionario.funcao.upper() == 'GESTOR':
                # Redireciona para a página do gestor
                return redirect('pagina_gestor')
            else:
                # Redireciona para a página do funcionário
                return redirect('pagina_funcionario')
            
            
        else:
            return HttpResponse('Usuário não cadastrado. <a href="/cadastrar_funcionario/">Cadastrar Funcionário</a>')
    # Retorna o template de login
    return render(request, 'login.html')  

# Página para gestores
def pagina_gestor(request):
    return render(request, 'pagina_gestor.html') 

# Página para funcionários
def pagina_funcionario(request):
    return render(request, 'pagina_funcionario.html')

#grazi
from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)

class PDF(models.Model):
    arquivo = models.FileField(upload_to='pdfs/')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
