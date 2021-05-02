from django.shortcuts import render

from .forms import RegForm
from .models import Registrado
# Create your views here.
def inicio(request):
    titulo = "HOLA"
    abc = "123"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)
    form = RegForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get("email")
        abc2 = form_data.get("nombre")
        obj = Registrado.objects.create(email = abc, nombre =abc2)

        #obj = Registrado()
        #obj.email = abc
        #obj.save()
    context = {
        "titulo": titulo, "el_form":form, "abc":abc,}
    return render(request, "inicio.html", context)