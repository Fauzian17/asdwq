from django.urls import path
from pengguna.views import formulir_list,home,formulir_view



urlpatterns = [
    path('', home, name='home'),
    path('formulir/list', formulir_list, name='formulir_list'),
    path('formulir/view',formulir_view, name='formulir_view'),
]