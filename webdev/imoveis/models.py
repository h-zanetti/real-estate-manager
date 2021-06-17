from django.db import models
from django.utils.translation import gettext_lazy as _

class Imovel(models.Model):
    # Referente ao imóvel em si
    ponto_de_referencia = models.CharField(_('ponto de referência'), max_length=75, null=True, blank=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    endereco = models.CharField(_('endereço'), max_length=200)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    # Referente a estadia
    ocupacao_maxima = models.IntegerField(_('ocupação máxima'))
    diaria = models.FloatField(_('diária'))
    class Meta:
        verbose_name = _('imóvel')
        verbose_name_plural = _('imóveis')