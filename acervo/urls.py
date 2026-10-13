from . import views
from django.urls import path

urlpatterns = [
    path('', views.pagina_inicial, name="pagina_inicial"),
    path("cadastrar-autor/",views.cadastrar_autor,name="cadastrar_autor"),
    path("cadastrar-livro/",views.cadastrar_livro,name="cadastrar_livro"),
    path("listar-autores/",views.lista_autores,name="lista_autores"),
]