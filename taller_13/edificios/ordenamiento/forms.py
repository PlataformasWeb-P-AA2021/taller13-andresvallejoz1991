from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from ordenamiento.models import Edificio, \
        Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo_edificio']
        labels = {
            'nombre': _('Ingrese nombre nombre del edificio'),
            'direccion': _('Ingrese direccion del edificio'),
            'ciudad': _('Ingrese cédula del edificio'),
            'tipo_edificio': _('Ingrese especificación del edificio'),
        }

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']

        if "L" in valor:
            raise forms.ValidationError("La ciudad no puede empezar con la letra L")
        return valor    

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_pro', 'costo_depar', 'numero_cuar','edificio']

    def clean_costo_depar(self):
        valor = self.cleaned_data['costo_depar']

        if valor > 100:
            raise forms.ValidationError("El costo del departamento no puede ser mayor a 100")
        return valor   

    def clean_numero_cuar(self):
        valor = self.cleaned_data['numero_cuar']

        if valor == 0 or valor > 7 :
            raise forms.ValidationError("No se pueden ingresar 0 o más de 7 departamentos")
        return valor

    def clean_nombre_pro(self):
        valor = self.cleaned_data['nombre_pro']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("El nombre no puede tener menos de tres letras")
        return valor

class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificios, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificios
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificios)

    class Meta:
        model = Departamento
        fields = ['nombre_pro', 'costo_depar', 'numero_cuar','edificio']

    def clean_costo_depar(self):
        valor = self.cleaned_data['costo_depar']

        if valor > 100:
            raise forms.ValidationError("El costo del departamento no puede ser mayor a 100")
        return valor    

    def clean_numero_cuar(self):
        valor = self.cleaned_data['numero_cuar']

        if valor == 0 or valor > 7 :
            raise forms.ValidationError("No se pueden ingresar 0 o más de 7 departamentos")
        return valor

    def clean_nombre_pro(self):
        valor = self.cleaned_data['nombre_pro']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("El nombre no puede tener menos de tres letras")
        return valor        

