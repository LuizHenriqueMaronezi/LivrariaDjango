from django.db import models

# Create your models here.

# o 'choices' tem que receber uma lista de tuplas -> o primeiro nome é o o valor interno do sistema
# o segundo valor é o jeito que vai aparecer na tela
GENEROS = [
    ("fantasia","Fantasia"),
    ("drama","Drama"),
    ("ficcao","Ficção"),
    ("aventura","Aventura"),
    ("comedia","Comédia"),
    ("biografia","Biografia"),
    ("terror","Terror"),
    ("autoajuda","Autoajuda"),
    ("religioso","Religioso"),
    ("suspense","Suspense"),
    ("romance","Romance")
]

# Como o Livro precisa conhecer Autor, o Autor tem que ser primeiro no código
 
class Autor(models.Model): # Não colocamos o livros = list(Livro) aqui, o django vai fazer isso
    nome = models.CharField(max_length=200, null=False)
    data_nascimento = models.DateField()
    aposentado = models.BooleanField()

    def __str__(self):
        return f"{self.nome}, {self.data_nascimento}, " "Aposentado" if self.aposentado else f"{self.nome}, {self.data_nascimento}"

class Livro(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    preco = models.DecimalField(null=False, max_digits=8, decimal_places=2)
    data_publicacao = models.DateField()

    #Relação um pra muitos no python 
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    genero = models.CharField(max_length=30,choices=GENEROS)

    def __str__(self):
        return f"{self.titulo}: R${self.preco}"