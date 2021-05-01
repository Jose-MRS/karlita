from django.shortcuts import render

from .forms import RegForm
# Create your views here.
def inicio(request):
    form = RegForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        print(form_data.get("nombre"))
        print(form_data.get("edad"))
    context = {"el_form":form,}
    return render(request, "inicio.html", context)