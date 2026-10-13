from django.shortcuts import render, redirect
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
        "cadastra_autor.html",
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
        "cadastra_livro.html",
        {"form":form}
    )

def lista_autores(request):
    autores = Autor.objects.all().order_by()

    return render(
        request,
        'lista_autores.html',
        {"autores": autores}
    )