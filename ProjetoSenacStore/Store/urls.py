
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('teste/', views.teste, name = 'teste'),
    path('departamentos/',views.departamentos, name = 'departamentos'),
    path('categorias/<int:id>',views.categorias, name = 'categorias'),
    path('produtos/<int:id>',views.produtos, name = 'produtos'),
    path('detalhes/<int:id>',views.detalhes, name = 'detalhes')

]