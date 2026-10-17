from . import views
from django.urls import path

urlpatterns = [
    path('', views.pagina_inicial, name="pagina_inicial"),
    path("cadastrar-autor/",views.cadastrar_autor,name="cadastrar_autor"),
    path("cadastrar-livro/",views.cadastrar_livro,name="cadastrar_livro"),
    path("listar-autores/",views.lista_autores,name="lista_autores"),
    path("livro/<int:pk>", views.detalhes_livro,name="detalhes_livro"),
    path("livro/editar/<int:pk>", views.editar_livro,name="editar_livro"),
    path("autor/<int:pk>", views.detalhes_autor, name="detalhes_autor"),
    path("livro/deletar/<int:pk>", views.deletar_livro, name="deletar_livro"),
    path("autor/deletar/<int:pk>", views.deletar_autor, name="deletar_autor")
]