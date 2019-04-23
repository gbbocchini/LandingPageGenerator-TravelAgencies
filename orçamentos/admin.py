from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.core.mail import send_mail

admin.site.register(Origem)
admin.site.register(Loja)
admin.site.register(Agente)
admin.site.register(Status)
# admin.site.register(Orçamento)


@admin.register(Orçamento)
class OrçamentoAdmin(admin.ModelAdmin):
    readonly_fields = ["referencia", "hora_inclusao", "solicitação"]
    date_hierarchy = 'hora_inclusao'
    list_display = ('referencia', 'direcionado_para', 'texto_solicitação', 'hora_atualização', 'status', )
    list_filter = ('direcionado_para', 'status')
    actions = ["Enviar_Emails"]

    def solicitação(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.img_solicitação.url,
            width=obj.img_solicitação.width,
            height=obj.img_solicitação.height,
        )
        )

    def Enviar_Emails(self, request, queryset):
        for i in queryset:
            if i.email_solicitante:
                message = str(i.texto_solicitação+" "+i.email_solicitante+" "+i.telefone_whatsapp_solicitante)
                send_mail(
                "Solicitação de: "+i.nome_solicitante,
                message,
                '',
                [i.enviar_este_pedido_para_1, i.enviar_este_pedido_para_2, i.enviar_este_pedido_para_3, i.enviar_este_pedido_para_4]
                fail_silently=False)
            else:
                pass

