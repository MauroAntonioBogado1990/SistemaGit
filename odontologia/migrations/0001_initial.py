# Generated by Django 3.2.3 on 2021-09-14 14:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(blank=True, max_length=50, null=True, verbose_name='dia del calendario')),
                ('hora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('razon_Social', models.CharField(max_length=100, verbose_name='Razon Social')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('telefono', models.CharField(blank=True, max_length=50, null=True, verbose_name='N°de telefono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('web', models.CharField(blank=True, max_length=50, null=True, verbose_name='Página web')),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cp', models.IntegerField(verbose_name='Código Postal')),
            ],
            options={
                'verbose_name_plural': 'Localidades',
            },
        ),
        migrations.CreateModel(
            name='ObraSocial',
            fields=[
                ('nombreOS', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Obra Social')),
                ('direccion', models.CharField(max_length=120)),
                ('disponible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('num_doc', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='N° de documento')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre/s')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido/s')),
                ('num_cuit', models.CharField(blank=True, max_length=20, null=True, verbose_name='N° de CUIT')),
                ('fecha_nac', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Nacimiento')),
                ('telefono', models.CharField(blank=True, max_length=50, null=True, verbose_name='N°de telefono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('direccion', models.CharField(max_length=120)),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='persona_localidad', to='odontologia.localidad')),
            ],
            options={
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='PiezaDental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Prestacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(blank=True, max_length=20, null=True, verbose_name='matricula')),
                ('dias', models.CharField(blank=True, max_length=50, null=True, verbose_name='Dias de Turno')),
                ('horario', models.CharField(blank=True, max_length=50, null=True, verbose_name='horario de turno')),
                ('especialidad', models.CharField(blank=True, max_length=30, null=True, verbose_name='especialidad')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='profesional', to='odontologia.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True, verbose_name='nombre')),
                ('contraseña', models.CharField(blank=True, max_length=20, null=True, verbose_name='contraseña')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuario', to='odontologia.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de tratamiento')),
                ('observacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Observacion')),
                ('medicoEfector', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='odontologia.profesional')),
                ('prestacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='odontologia.prestacion')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('numHisCli', models.CharField(max_length=250, primary_key=True, serialize=False, verbose_name='N° de Historia Clinica')),
                ('numObraSocial', models.CharField(blank=True, max_length=30, null=True, verbose_name='N° de Obra Social')),
                ('titular_familiar', models.CharField(blank=True, max_length=200, null=True, verbose_name='titular familiar')),
                ('obraSoc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='obraSocial_paciente', to='odontologia.obrasocial')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='paciente', to='odontologia.persona')),
            ],
        ),
        migrations.CreateModel(
            name='FichaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_alta', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Alta')),
                ('tipo_sangre', models.CharField(blank=True, max_length=10, null=True, verbose_name='Tipo de Sangre')),
                ('antecedentes', models.CharField(blank=True, max_length=250, null=True, verbose_name='Antecedentes')),
                ('medicacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Medicación')),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='establecimiento_localidad', to='odontologia.establecimiento')),
                ('historiaClinica', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='odontologia.tratamiento')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='odontologia.paciente')),
                ('prestacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='odontologia.prestacion')),
            ],
        ),
        migrations.CreateModel(
            name='Ficha_Tratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichaMedica', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='odontologia.fichamedica')),
                ('tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='odontologia.tratamiento')),
            ],
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='odontologia.localidad'),
        ),
        migrations.CreateModel(
            name='Calendario_turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_hora', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='diaHoraCalendario', to='odontologia.calendario')),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='profesionalCalendario', to='odontologia.profesional')),
            ],
        ),
    ]
