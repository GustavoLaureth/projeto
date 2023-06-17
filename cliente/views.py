from django.shortcuts import render, redirect
from .models import Cliente
from .form import ClienteForm
from django.contrib import messages
from django.core.paginator import Paginator
from .filters import ClienteFilter
from django.core.mail import send_mail

def cliente(request):
    # list_clientes = Cliente.objects.all()
    list_clientes = Cliente.objects.order_by('-data_criacao')
    myFilter = ClienteFilter(request.GET, queryset=list_clientes)
    list_clientes = myFilter.qs
    paginator = Paginator(list_clientes, 8)
    page = request.GET.get('page')
    list_clientes = paginator.get_page(page)
    return render(request, 'cliente/cliente.html', {'clientes': list_clientes, 'myFilter': myFilter})

def detalhe(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    return render(request, 'cliente/detalhe.html', {'cliente': cliente})

def form(request):
    data = {}
    data['form'] = ClienteForm()
    return render(request, 'cliente/form.html', data)

def create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Empenho cadastrado com sucesso.')
            return redirect('cliente')
    else:
        form = ClienteForm()

def edit(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(instance=cliente)
    return render(request, 'cliente/form.html', {'cliente': cliente, 'form': form})

def update(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST, request.FILES, instance=cliente)
    if form.is_valid():
        if request.POST['categoria'] == "1":
            send_mail(
                'Recebemos o Empenho',
                'Recebemos o Pedido, iremos passar agora para o setor responsável, assim que possivel enviaremos o código de rastreio',
                'gustavolaureth22@gmail.com',
                [cliente.email],
                fail_silently=False
            )
        if request.POST['categoria'] == "3":
            send_mail(
                'Pedido Enviado',
                'O seu Pedido foi enviado, segue código de restreio',
                'gustavolaureth22@gmail.com',
                [cliente.email],
                fail_silently=False
            )
        form.save()
        messages.add_message(request, messages.INFO, 'Empenho atualizado com sucesso.')
        return redirect('cliente')

def delete(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    messages.add_message(request, messages.ERROR, 'Empenho excluido com sucesso.')
    return redirect('cliente')
