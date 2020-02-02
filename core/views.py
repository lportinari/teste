from django.shortcuts import render
from django.contrib import messages  # Adiciona mensagens no contexto da página

from .forms import ContatoForm


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)  # Este formulário pode ter dados ou não (Quando usuário envia o formulário
    # ou quando carrega a página)

    if str(request.method) == 'POST':
        print(f'Posta: {request.POST}')
        if form.is_valid():
            # Se o formulário for válido as variáveis pegam o valor (form name)
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada!')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'E-mail enviado com sucesso!')  # Mensagem de sucesso!
            form = ContatoForm()
        else:
            messages.error(request, "Erro ao enviar e-mail!")  # Mensagem de erro!

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')
