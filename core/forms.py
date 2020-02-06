from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='nome', max_length=50)
    email = forms.EmailField(label='E-mail', max_length=50)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        # Formatação do e-mail
        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='Email enviado pelo sistema',  # Assunto
            body=conteudo,
            from_email='contato@seudominio.com',
            to=['contato@seudominio.com', ],  # Seu e-mail. POde adicionar quantos e-mails quiser
            headers={'Reply-To': email}  # Email para qual responder
        )
        # Envia o e-mail de acordo com o que setamos no settings
        mail.send()
