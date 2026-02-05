from django import forms
from .models import Paciente



class PacienteForm(forms.ModelForm):
    foto_perfil = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )
    foto_resultado = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )


    class Meta:
        model = Paciente
        fields = [
            'id',
            'nombre',
            'edad',
            'sexo',
            'email',
            'telefono',
            'texto',
            'foto_perfil',
            'foto_resultado',
        ]

        widgets = {
            'id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Código alfanumérico'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad'
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email@correo.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '55-2478-5578'
            }),
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
