from .forms import Formulario
from .models import Pacote
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.core.mail import send_mail


# List view no index (caso user saia da landing page)
class PacoteList(ListView):
    model = Pacote
    context_object_name = 'pacote'
    template_name = 'index.html'

#template genérico indicando sucesso ao user
class Sucesso(TemplateView):
     template_name = 'sucesso.html'


#View mista: model+form de contato
class PacoteView(DetailView, FormMixin):
    model = Pacote
    context_object_name = 'pacote_detail'
    template_name = 'base.html'
    form_class = Formulario

    def get_context_data(self, *args, **kwargs):
        context = super(PacoteView, self).get_context_data(*args, **kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, slug):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            lista_itens = ['hotel_pref', 'quarto_pref', 'nome_do_interessado', 'quer_viajar_em_outra_data',
                           'email_contato', 'telefone_contato']
            lista = []
            for i in lista_itens:
                lista.append(form.cleaned_data.get(i))
            subject = "Solicitação da Landing Page: "+request.POST.get('site_e_termos')
            message = str(lista)
            from_email = 'landing@pacotes.frontur.com.br'
            send_mail(subject, message, from_email, ['marketing@frontur.com.br'])
            form.save(commit=True)
            return HttpResponseRedirect('/sucesso/')
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
          if form.is_valid:
              form.save(commit=True)
          return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('pacote', kwargs={'slug': self.object.slug})

