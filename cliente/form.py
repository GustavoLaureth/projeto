from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate

from .models import Cliente, Account


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Login inválido!')


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['numero', 'nome', 'cnpj', 'data_criacao', 'categoria', 'empresa', 'empenho', 'descricao', 'valor', 'nfe', 'n_nfe']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field]. widget.attrs.update({'class': 'form-control'})
