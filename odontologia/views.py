from django.shortcuts import render, redirect

from .models import Persona
from .forms import PersonaForm
# Create your views here.


def index(request, template_name='odontologia/index.html'):
    return render(request, template_name)


def personas_listar(request, template_name='odontologia/pacientes.html'):
    personas = Persona.objects.all()
    dato_personas = {"personas": personas}
    return render(request, template_name, dato_personas)


def nuevo_paciente(request, template_name='odontologia/paciente_form.html'):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('pacientes')
        else:
            print(form.errors)
    else:
        form = PersonaForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def modificar_paciente(request, pk, template_name='odontologia/paciente_form.html'):
    paciente = Persona.objects.get(num_doc=pk)
    form = PersonaForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save(commit=True)
        return redirect('pacientes')
    else:
        print(form.errors)
    datos = {'form': form}
    return render(request, template_name, datos)


def eliminar_paciente(request, pk, template_name='odontologia/paciente_confirmar_eliminacio.html'):
    paciente = Persona.objects.get(num_doc=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes')
    else:
        dato = {'form': paciente}
        return render(request, template_name, {'form': paciente})
