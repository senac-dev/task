from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('concluir/<int:id>/', views.concluir_tarefa, name='concluir_tarefa'),
]


