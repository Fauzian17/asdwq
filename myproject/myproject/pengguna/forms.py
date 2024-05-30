from django import forms
from pengguna.models import Formulir

class FormulirForm(forms.ModelForm):
    class Meta:
        model = Formulir
        fields = '__all__'  # Ensure all required fields are included
