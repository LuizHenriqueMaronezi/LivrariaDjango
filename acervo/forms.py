from django import forms
from .models import Livro, Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

        widgets = {
                    'data_nascimento': forms.DateInput(attrs={'type':'date'})
                }

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

        widgets = {
            'data_publicacao': forms.DateInput(attrs={'type':'date'})
        }