from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado
# Create your views here.
def inicio(request):
    titulo = "Bienvenido formulario de registro"
    abc = "123"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)

    context = {
        "titulo": titulo, "el_form":form, "abc":abc,}
    if form.is_valid():
        instance = form.save(commit=False)
        #if not instance.nombre:
            #instance.nombre = "PERSONA"
        instance.save()

        context = {
            "titulo": "Gracias %s!" %(instance.nombre)
        }
        if not instance.nombre:
            #context = { "titulo": "Gracias señor de incógnito"}
            context ={"titulo": "Gracias %s" %(instance.email)}
        print (instance)
        print (instance.timestamp)
        #form_data = form.cleaned_data
        #abc = form_data.get("email")
        #abc2 = form_data.get("nombre")
        #obj = Registrado.objects.create(email = abc, nombre =abc2)

        #obj = Registrado()
        #obj.email = abc
        #obj.save()

    return render(request, "inicio.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        #for key, value in form.cleaned_data.items():
         #   print(key, value)
        #for key in form.cleaned_data:
         #   print (key)
          #  print (form.cleaned_data.get(key))
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = 'Form e Contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "otroemail@gamil.com"]
        email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
        send_mail(asunto, 
            email_mensaje,
            email_from,
            email_to,
            fail_silently = False
            )
        #print (email, mensaje, nombre)
    context ={"form":form,}
    return render(request, "forms.html", context)