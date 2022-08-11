
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name = 'index'),
    path('teste/', views.teste, name = 'teste'),
    path('departamentos/',views.departamentos, name = 'departamentos'),
    path('categorias/<int:id>',views.categorias, name = 'categorias'),
    path('produtos/<int:id>',views.produtos, name = 'produtos'),
    path('produto_detalhe/<int:id>',views.produto_detalhe, name = 'produto_detalhe'),
    path('institucional/', views.institucional, name='institucional'),
    path('contato/', views.contato, name='contato'),
    path('contato/enviar/', views.enviar_email, name='enviar_contato')

]


# Deploy com Heroku
#Url: https://www.heroku.com/
#Tutorial: https://www.treinaweb.com.br/blog/deploy-de-uma-aplicacao-django-no-heroku

#priorizar este :
#Deploy com PythonAnyWhere
#Url: https://www.pythonanywhere.com/
#Tutorial: https://acervolima.com/como-implantar-o-projeto-django-no-pythonanywhere/
#Linbk do projeto
#http://github.com/profronicosta/ProjetoSenacStore

#ronivaldo.pcosta@sp.senac.br
