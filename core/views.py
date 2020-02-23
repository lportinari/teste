from django.shortcuts import render
from django.contrib import messages  # Adiciona mensagens no contexto da página
from django.shortcuts import redirect

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)  # Este formulário pode ter dados ou não (Quando usuário envia o formulário
    # ou quando carrega a página)

    if str(request.method) == 'POST':
        if form.is_valid():
            # Se o formulário for valido. envie o e-mail.
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')  # Mensagem de sucesso!
            form = ContatoForm()
        else:
            messages.error(request, "Erro ao enviar e-mail!")  # Mensagem de erro!

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)  # Request.files por que tem upload de arquivo
            if form.is_valid():
                form.save()

                messages.success(request, 'Produto salvo com sucesso!')
                # limpar o formulário após submetido
                form = ProdutoModelForm()

            else:
                messages.error(request, 'Erro ao cadastro produto!')
        else:
            form = ProdutoModelForm()

        context = {
            'form': form
        }
        return render(request, 'produto.html', context)

    else:
        return redirect('index')
