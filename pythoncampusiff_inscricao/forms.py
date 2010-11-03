from django import forms
from django.contrib.localflavor.br.forms import BRCPFField
from models import Inscrito

class FormularioDeInscrito(forms.ModelForm):
    cpf = BRCPFField(label='CPF')

    class Meta:
        model = Inscrito
        exclude = ('estado','minicurso_da_manha','minicurso_da_tarde')