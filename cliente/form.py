from django.forms import ModelForm
from .models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['numero', 'nome', 'cnpj', 'data_criacao', 'categoria', 'empresa', 'empenho', 'descricao', 'valor', 'nfe', 'n_nfe', 'email']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field]. widget.attrs.update({'class': 'form-control'})
