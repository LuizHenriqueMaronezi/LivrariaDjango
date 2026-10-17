from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Autor
from .forms import LivroForm, AutorForm

# Create your views here.

def pagina_inicial(request):
    livros = Livro.objects.all().order_by()

    return render(
        request,
        'pagina_inicial.html',
        {"livros": livros}
    )

def cadastrar_autor(request):

    if request.method == "POST":
        form = AutorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista_autores")

    else:
        form = AutorForm()

    return render(
        request,
        "autor/cadastra_autor.html",
        {"form": form}
    )

def cadastrar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("pagina_inicial")

    else:
        form = LivroForm()

    return render(
        request,
        "livro/cadastra_livro.html",
        {"form":form}
    )

def lista_autores(request):
    autores = Autor.objects.all().order_by()

    return render(
        request,
        'autor/lista_autores.html',
        {"autores": autores}
    )

def detalhes_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)

    return render(
        request,
        'livro/detalhes_livro.html',
        {"livro": livro}
    )

def detalhes_autor(request,pk):
    autor = get_object_or_404(Autor, pk=pk)

    return render(
        request,
        'autor/detalhes_autor.html',
        {"autor": autor}
    )

def deletar_autor(request,pk):
    autor = get_object_or_404(Autor,pk=pk)

    if request.method == "POST":
        autor.delete()
        return redirect("pagina_inicial")

    else:
        return redirect("pagina_inicial")

def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)

    if request.method == "POST":
        form_editado = LivroForm(request.POST, instance=livro)

        if form_editado.is_valid():
            form_editado.save()

            return redirect("detalhes_livro", pk=livro.pk)

    else:
        form = LivroForm(instance=livro)

    return render(
        request,
        'livro/editar_livro.html',
        {"form": form}
    )

def deletar_livro(request,pk):
    livro = get_object_or_404(Livro,pk=pk)

    if request.method == "POST": # Caso tenha pedido para excluir -> O navegador só entende req POST
        livro.delete()
        return redirect("pagina_inicial")

    else: # Caso tenha digitado o path no navegador em vez de apertar o botão, foi apenas um GET
        return redirect("pagina_inicial") # Aí redirecina para a pagina inicial