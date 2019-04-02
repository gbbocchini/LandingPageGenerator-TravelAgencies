from django.db import models

#modelo pacotes, infos injetadas no template base.html. Acesso via slug definida pelo cadastrante do pacote
class Pacote(models.Model):
    banner = models.ImageField(upload_to='imagens', blank=True)
    nome = models.CharField(max_length=50)
    voos = models.ImageField(upload_to='imagens', blank=False)
    descritivo = models.TextField()

    hotel_1 = models.CharField(max_length=100)
    hotel_1_site = models.URLField(max_length=50)
    hotel_1_tripadvisor = models.URLField(max_length=100)
    hotel_1_avaliacao = models.ImageField(upload_to='imagens')
    hotel_1_valor_1_adulto = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_1_valor_2_adultos = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_1_valor_2_adultos_1_chd = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_1_valor_2_adultos_2_chd = models.DecimalField(max_digits=10, decimal_places=2)

    hotel_2 = models.CharField(max_length=100)
    hotel_2_site = models.URLField(max_length=50)
    hotel_2_tripadvisor = models.URLField(max_length=100)
    hotel_2_avaliacao = models.ImageField(upload_to='imagens')
    hotel_2_valor_1_adulto = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_2_valor_2_adultos = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_2_valor_2_adultos_1_chd = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_2_valor_2_adultos_2_chd = models.DecimalField(max_digits=10, decimal_places=2)

    hotel_3 = models.CharField(max_length=100)
    hotel_3_site = models.URLField(max_length=50)
    hotel_3_tripadvisor = models.URLField(max_length=100)
    hotel_3_avaliacao = models.ImageField(upload_to='imagens')
    hotel_3_valor_1_adulto = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_3_valor_2_adultos = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_3_valor_2_adultos_1_chd = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_3_valor_2_adultos_2_chd = models.DecimalField(max_digits=10, decimal_places=2)

    publicado = models.BooleanField(default=False)
    slug = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


#modelo formulário dentro da landing page (siteForeigKey é hidden==True, indicativo interno para a empresa)
class ContatoForm(models.Model):

    site_e_termos = models.ForeignKey(Pacote, on_delete='CASCADE')

    hotel_pref = models.CharField(max_length=50, blank=False)

    quarto_pref = models.CharField(max_length=50, blank=False)

    nome_1 = models.CharField(max_length=150, blank=False)
    data_nascimento_1 = models.DateField(blank=False)

    nome_2 = models.CharField(max_length=150, blank=True, null=True)
    data_nascimento_2 = models.DateField(blank=True, null=True)

    nome_3 = models.CharField(max_length=150, blank=True, null=True)
    data_nascimento_3 = models.DateField(blank=True, null=True)

    nome_4 = models.CharField(max_length=150, blank=True, null=True)
    data_nascimento_4 = models.DateField(blank=True, null=True)

    email_contato = models.EmailField(blank=False)

    telefone_contato = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.email_contato


