
#definição das rotas de um app
#ligando as URLs às views que processarão as requisições e 
#organizando a navegação da aplicação

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #página de cadastro de funcionário
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    # funcionário cadastrado
    path('cadastrar_funcionario/sucesso/', views.cadastro_sucesso, name='cadastrar_funcionario_sucesso'), 
    #pagina de login
    path('login/', views.login_view, name='login'), 
    # Página inicial pós-login
    #path('pagina_inicial/', views.pagina_inicial, name='pagina_inicial'),
    # Gestor 
    path('pagina_gestor/', views.pagina_gestor, name='pagina_gestor'),
    #Funcionário
    path('pagina_funcionario/', views.pagina_funcionario, name='pagina_funcionario')
]


#grazi
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_pdf, name='upload_pdf'),
    # outras rotas
]

