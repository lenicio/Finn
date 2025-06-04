from django.db import models


class BaseModel(models.Model):

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data do lançamento',
        help_text='data do lançamento'
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Data da última atualização',
        help_text='última atualização'
    )


    class Meta:
        abstract = True

