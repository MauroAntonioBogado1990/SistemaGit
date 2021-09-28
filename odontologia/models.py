from django.db import models
from datetime import datetime

from django.db.models.fields import DateField

# Create your models here.


class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    cp = models.IntegerField("Código Postal")

    class Meta:
        verbose_name_plural = 'Localidades'


def __str__(self):
    return self.nombre


class Persona(models.Model):
    num_doc = models.CharField(
        "N° de documento", max_length=20, primary_key=True)
    nombre = models.CharField("Nombre/s", max_length=150)
    apellido = models.CharField("Apellido/s", max_length=100)
    num_cuit = models.CharField(
        "N° de CUIT", max_length=20, null=True, blank=True)
    fecha_nac = models.DateField("Fecha de Nacimiento", default=datetime.now)
    telefono = models.CharField(
        "N°de telefono", max_length=50, null=True, blank=True)
    email = models.EmailField("E-mail", null=True, blank=True)
    direccion = models.CharField(max_length=120)
    localidad = models.ForeignKey(
        Localidad, on_delete=models.PROTECT, related_name='persona_localidad')

    class Meta:
        ordering = ["apellido", "nombre"]


def __str__(self):
    return '%s, %s' % (self.apellido, self.nombre)


class ObraSocial(models.Model):
    nombreOS = models.CharField("Obra Social", max_length=20, primary_key=True)
    direccion = models.CharField(max_length=120)
    disponible = models.BooleanField()


def __str__(self):
    return self.nombreOS


# Herencia de Persona --> Paciente


class Paciente(models.Model):
    paciente = models.ForeignKey(
        Persona, on_delete=models.PROTECT, related_name='paciente')
    numHisCli = models.CharField(
        "N° de Historia Clinica", max_length=250, primary_key=True)
    obraSoc = models.ForeignKey(
        ObraSocial, on_delete=models.PROTECT, related_name='obraSocial_paciente')
    numObraSocial = models.CharField(
        "N° de Obra Social", max_length=30, null=True, blank=True)
    titular_familiar = models.CharField(
        "titular familiar", max_length=200, null=True, blank=True)


def __str__(self):
    return self.nombre


# Herencia de Persona --> Usuario


class Usuario(models.Model):
    persona = models.ForeignKey(
        Persona, on_delete=models.PROTECT, related_name='usuario')
    nombre = models.CharField("nombre", max_length=200, null=True, blank=True)
    contraseña = models.CharField(
        "contraseña", max_length=20, null=True, blank=True)


def __str__(self):
    return self.nombre


# Herencia de Persona --> Profesional


class Profesional(models.Model):
    persona = models.ForeignKey(
        Persona, on_delete=models.PROTECT, related_name='profesional')
    matricula = models.CharField(
        "matricula", max_length=20, null=True, blank=True)
    dias = models.CharField(
        "Dias de Turno", max_length=50, null=True, blank=True)
    horario = models.CharField(
        "horario de turno", max_length=50, null=True, blank=True)
    especialidad = models.CharField(
        "especialidad", max_length=30, null=True, blank=True)


def __str__(self):
    return self.nombre


class Establecimiento(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    razon_Social = models.CharField("Razon Social", max_length=100)
    direccion = models.CharField("Dirección", max_length=100)
    localidad = models.ForeignKey(
        Localidad, on_delete=models.PROTECT)
    telefono = models.CharField(
        "N°de telefono", max_length=50, null=True, blank=True)
    email = models.EmailField("E-mail", null=True, blank=True)
    web = models.CharField("Página web", max_length=50, null=True, blank=True)


def __str__(self):
    return self.nombre


class Prestacion(models.Model):
    nombre = models.CharField("Nombre", max_length=120, null=False)
    descripcion = models.CharField("Descripción", max_length=300, null=False)
    # piezaDental=models.ForeingKey(PiezaDental, on_delete=models.PROTECTED, related_named='prestacion_piezaDental')


def __str__(self):
    return self.nombre


class PiezaDental(models.Model):
    nombre = models.CharField("Nombre", max_length=200, null=False)

    def __str__(self) -> str:
        return self.nombre


class Tratamiento(models.Model):
    medicoEfector = models.ForeignKey(
        Profesional, on_delete=models.PROTECT)
    prestacion = models.ForeignKey(
        Prestacion, on_delete=models.PROTECT)
    fecha = models.DateField("Fecha de tratamiento", default=datetime.now)
    observacion = models.CharField(
        "Observacion", max_length=200, null=True, blank=True)


def __str__(self):
    return self.prestacion


class FichaMedica(models.Model):
    establecimiento = models.ForeignKey(
        Establecimiento, on_delete=models.PROTECT, related_name='establecimiento_localidad')
    paciente = models.ForeignKey(
        Paciente, on_delete=models.PROTECT)
    fecha_alta = models.DateField("Fecha de Alta", default=datetime.now)
    tipo_sangre = models.CharField(
        "Tipo de Sangre", max_length=10, null=True, blank=True)
    antecedentes = models.CharField(
        "Antecedentes", max_length=250, null=True, blank=True)
    medicacion = models.CharField(
        "Medicación", max_length=200, null=True, blank=True)
    prestacion = models.ForeignKey(
        Prestacion, on_delete=models.PROTECT)
    historiaClinica = models.ForeignKey(
        Tratamiento, on_delete=models.PROTECT)


def __str__(self):
    return self.historiaClinica


class Ficha_Tratamiento(models.Model):
    fichaMedica = models.ForeignKey(
        FichaMedica, on_delete=models.PROTECT)
    tratamiento = models.ForeignKey(
        Tratamiento, on_delete=models.PROTECT)


def __str__(self):
    return self.fichaMedica

# calendario


class Calendario(models.Model):
    dia = models.CharField("dia del calendario",
                           max_length=50, null=True, blank=True)
    hora = models.DateTimeField()


def __str__(self):
    return self.dia

# calendario Turnos


class Calendario_turnos(models.Model):
    profesional = models.ForeignKey(
        Profesional, on_delete=models.PROTECT, related_name='profesionalCalendario')
    dia_hora = models.ForeignKey(
        Calendario, on_delete=models.PROTECT, related_name='diaHoraCalendario')


def __str__(self):
    return self.profesional
