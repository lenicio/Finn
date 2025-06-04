from django.contrib import admin
from apps.financa.models.transacao import Transacao


@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ['tipo_transacao', 'descricao', 'valor', 'data_transacao', 'status_transacao']
    list_filter = ['tipo_transacao', 'status_transacao']
    search_fields = ['descricao', 'valor']
    list_per_page = 20
    readonly_fields = ['criado_em', 'atualizado_em']
    fieldsets = [
        ('Informações sobre transação',
         {
             'fields': ['tipo_transacao', 'descricao', 'valor', 'data_transacao', 'status_transacao']
         }
        ),

        ('Informações Extras',
            {   'classes': ['collapse'],
                'fields': ['criado_em', 'atualizado_em']
            }
        )
    ]