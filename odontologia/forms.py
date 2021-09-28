from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Calendario, Calendario_turnos, Ficha_Tratamiento, Localidad, Persona, Establecimiento, FichaMedica, ObraSocial, Paciente, PiezaDental, Prestacion, Profesional, Tratamiento, Usuario

# creando el dato de tipo de calendario


class DateInput(forms.DateInput):
    input_type = 'date'


class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize'}),
            'apellido': forms.TextInput({'class': 'form-control input', 'text-transform': 'capitalize'}),
            'cuit': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize'}),
            'fecha_nac': DateInput(format='%Y-%m-%d', attrs={'class': 'form-control input-sm'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control input'}),
            'email': forms.TextInput(attrs={'class': 'form-control input'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control input'}),
            'localidad': forms.Select(attrs={'class': 'form-control input'}),
        }


class CalendarioForm(ModelForm):
    class Meta:
        model = Calendario
        fields = '__all__'


class CalendarioTurnosForm(ModelForm):
    class Meta:
        model = Calendario_turnos
        fields = '__all__'


class EstablecimientoForm(ModelForm):
    class Meta:
        model = Establecimiento
        fields = '__all__'


class FichaMedicaForm(ModelForm):
    class Meta:
        model = FichaMedica
        fields = '__all__'


class FichaTratamientoForm(ModelForm):
    class Meta:
        model = Ficha_Tratamiento
        fields = '__all__'


class ObraSocialForm(ModelForm):
    class Meta:
        model = ObraSocial
        fields = '__all__'


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'


class PiezaDentalForm(ModelForm):
    class Meta:
        model = PiezaDental
        fields = '__all__'


class PrestacionForm(ModelForm):
    class Meta:
        model = Prestacion
        fields = '__all__'


class ProfesionalForm(ModelForm):
    class Meta:
        model = Profesional
        fields = '__all__'


class TratamientoForm(ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
