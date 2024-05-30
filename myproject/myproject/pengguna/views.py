from django.shortcuts import render,redirect
from pengguna.models import Formulir
from pengguna.forms import FormulirForm

# Create your views here.

def home(request):
    template = "index.html"
    context = {
        'title': 'Home',
    }
    return render(request, template, context)

def formulir_list(request):
    template = "admin.html"
    formulir_list = Formulir.objects.all()
    print(formulir_list)
    context = {
        'title': 'Form Pendaftaran',
        'formulir_list': formulir_list
    }
    return render(request, template, context)

def akun_pengguna(request):
    template = "akun_pengguna.html"
    context = {
        'title': 'Akun Pengguna',
    }
    return render(request, template, context)
    
def formulir_view(request):
    print(request.user)
    template= "dashboard/snippets/formulir.html"
    if request.method == "POST":
        form = FormulirForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('{% url "dashboard" %}')
        else:
            print("Form is invalid")
            print(form.errors)  # Print form errors
            print(request.POST)  # Print POST data for debugging
    else:
        form = FormulirForm()
    context = {
        'title': 'Formulir',
        'form': form
    }
    return render(request, template, context)