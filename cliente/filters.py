import django_filters
from .models import Cliente


class ClienteFilter(django_filters.FilterSet):
    numero = django_filters.CharFilter(lookup_expr='icontains')
    n_nfe = django_filters.CharFilter(lookup_expr='icontains')
    nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cliente
        fields = '__all__'

        exclude = ['data_criacao', 'empenho', 'nfe', 'email']