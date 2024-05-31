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
    template = "dashboard/snippets/formulir_view.html"
    
    if request.method == "POST":
        form = FormulirForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace with your desired redirect URL
        else:
            print("Form is invalid")
            print(form.errors)  # Print form errors for debugging
    else:
        form = FormulirForm()

    context = {
        'title': 'Formulir',
        'form': form
    }
    return render(request, template, context)

def create_formulir(request):
    template='dashboard/snippets/formulir.html'
    if request.method == "POST":
        form = FormulirForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Ganti dengan URL halaman sukses Anda
    else:
        form = FormulirForm()

    context={
        'form': form, 
        'title': 'Buat Formulir Baru'
        }

    return render(request,template, context)
