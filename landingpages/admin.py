from django.contrib import admin
from .models import Pacote, ContatoForm

# admin.site.register(Pacote)
admin.site.register(ContatoForm)


@admin.register(Pacote)
class PacoteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'publicado')
    list_filter = ('nome', 'slug', 'publicado')
