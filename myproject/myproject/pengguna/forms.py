from django import forms
from .models import Formulir

class FormulirForm(forms.ModelForm):
    class Meta:
        model = Formulir
        fields = (
            'nama',
            'email',
            'tempat_lahir', 
            'tanggal_lahir', 
            'nik', 
            'no_hp', 
            'no_hp_ortu', 
            'alamat', 
            'kelurahan', 
            'kecamatan', 
            'kabupaten', 
            'jenis_kelamin', 
            'prodi1', 
            'prodi2', 
            'prodi3',
            'foto'
        )
        widgets = {
            "nama": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.EmailInput(attrs={'class':'form-control'}),
            "tempat_lahir": forms.TextInput(attrs={'class':'form-control'}),
            "tanggal_lahir": forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            "nik": forms.TextInput(attrs={'class':'form-control'}),
            "no_hp": forms.TextInput(attrs={'class':'form-control'}),
            "no_hp_ortu": forms.TextInput(attrs={'class':'form-control'}),
            "alamat": forms.Textarea(attrs={'class':'form-control'}),
            "kelurahan": forms.TextInput(attrs={'class':'form-control'}),
            "kecamatan": forms.TextInput(attrs={'class':'form-control'}),
            "kabupaten": forms.TextInput(attrs={'class':'form-control'}),
            "jenis_kelamin": forms.Select(attrs={'class':'form-control'}),
            "prodi1": forms.Select(attrs={'class':'form-control'}),
            "prodi2": forms.Select(attrs={'class':'form-control'}),
            "prodi3": forms.Select(attrs={'class':'form-control'}),
            "foto": forms.FileInput(attrs={'class':'form-control'}),
        }

# class FormulirForm(forms.ModelForm):
#     class Meta:
#         model = Formulir
#         fields = ['nama', 'email', 'tempat_lahir', 'tanggal_lahir', 'nik', 'no_hp', 'no_hp_ortu', 'alamat', 'kelurahan', 'kecamatan', 'kabupaten', 'jenis_kelamin', 'prodi1', 'prodi2', 'prodi3', 'foto']
#         widgets = {
#             'tanggal_lahir': forms.DateInput(attrs={'type': 'date'}),
#             'jenis_kelamin': forms.Select(choices=[('Laki-Laki', 'Laki-Laki'), ('Perempuan', 'Perempuan')]),
#             'prodi1': forms.Select(choices=[
#                 ('S1 - Pendidikan Dokter', 'S1 - Pendidikan Dokter'),
#                 ('D4 - Analis Kesehatan', 'D4 - Analis Kesehatan'),
#                 ('S1 - Ilmu Kesehatan Masyarakat', 'S1 - Ilmu Kesehatan Masyarakat'),
#                 ('S1 - Gizi', 'S1 - Gizi'),
#                 ('S1 - PGSD', 'S1 - PGSD'),
#                 ('S1 - PGPAUD', 'S1 - PGPAUD'),
#                 ('S1 - Pendidikan Bahasa Inggris', 'S1 - Pendidikan Bahasa Inggris'),
#                 ('S1 - Akuntansi', 'S1 - Akuntansi'),
#                 ('S1 - Manajemen', 'S1 - Manajemen'),
#                 ('S1 - Sistem Informasi', 'S1 - Sistem Informasi'),
#                 ('S1 - Keperawatan', 'S1 - Keperawatan'),
#                 ('D3 - Keperawatan', 'D3 - Keperawatan'),
#                 ('D4 - Bidan', 'D4 - Bidan'),
#                 ('D3 - Kebidanan', 'D3 - Kebidanan')
#             ]),
#             'prodi2': forms.Select(choices=[
#                 ('S1 - Pendidikan Dokter', 'S1 - Pendidikan Dokter'),
#                 ('D4 - Analis Kesehatan', 'D4 - Analis Kesehatan'),
#                 ('S1 - Ilmu Kesehatan Masyarakat', 'S1 - Ilmu Kesehatan Masyarakat'),
#                 ('S1 - Gizi', 'S1 - Gizi'),
#                 ('S1 - PGSD', 'S1 - PGSD'),
#                 ('S1 - PGPAUD', 'S1 - PGPAUD'),
#                 ('S1 - Pendidikan Bahasa Inggris', 'S1 - Pendidikan Bahasa Inggris'),
#                 ('S1 - Akuntansi', 'S1 - Akuntansi'),
#                 ('S1 - Manajemen', 'S1 - Manajemen'),
#                 ('S1 - Sistem Informasi', 'S1 - Sistem Informasi'),
#                 ('S1 - Keperawatan', 'S1 - Keperawatan'),
#                 ('D3 - Keperawatan', 'D3 - Keperawatan'),
#                 ('D4 - Bidan', 'D4 - Bidan'),
#                 ('D3 - Kebidanan', 'D3 - Kebidanan')
#             ]),
#         }
