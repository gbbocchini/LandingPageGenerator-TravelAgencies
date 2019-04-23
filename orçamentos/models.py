from django.db import models


class Agente(models.Model):
    nome = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome


class Origem(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Status(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Loja(models.Model):
    nome = models.CharField(max_length=20)
    email_orçamentos = models.EmailField(max_length=50)
    agentes = models.ManyToManyField(Agente)

    def __str__(self):
        return self.nome



class Orçamento(models.Model):
    referencia = models.AutoField(primary_key=True, editable=False)
    origem = models.ForeignKey(Origem, on_delete='PROTECT')
    hora_inclusao = models.DateTimeField(auto_now_add=True)
    direcionado_para = models.ForeignKey(Loja, on_delete='PROTECT')
    enviar_este_pedido_para_1 = models.EmailField(max_length=50, default='email@email.com')
    enviar_este_pedido_para_2 = models.EmailField(max_length=50, blank=True, null=True)
    enviar_este_pedido_para_3 = models.EmailField(max_length=50, blank=True, null=True)
    enviar_este_pedido_para_4 = models.EmailField(max_length=50, blank=True, null=True)
    nome_solicitante = models.CharField(max_length=100)
    email_solicitante = models.EmailField(max_length=100)
    telefone_whatsapp_solicitante = models.CharField(max_length=20)
    cidade_ou_pais_solicitante = models.CharField(max_length=100, default="Brasil", blank=True, null=True)
    img_solicitação = models.ImageField(max_length=500, blank=True, null=True)
    texto_solicitação = models.TextField(max_length=500, blank=True, null=True)
    atendente_loja = models.ForeignKey(Agente, on_delete='PROTECT', null=True, blank=True)
    hora_atualização = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.ForeignKey(Status, on_delete='PROTECT')
    se_fechado_qual_valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    se_fechado_quant_pax = models.IntegerField(default=0)

    def __str__(self):
        return "{} {} {} {}".format(self.referencia, self.direcionado_para, self.texto_solicitação, self.status)
