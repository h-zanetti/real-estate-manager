from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.PositiveBigIntegerField(_('telefone'), blank=True, null=True)
    cpf = models.PositiveBigIntegerField(_('CPF'), unique=True, blank=True, null=True)

    username = None
    email = models.EmailField(_('endereço de email'), unique=True)
    first_name = models.CharField(_('nome'), max_length=30, blank=True, null=True)
    last_name = models.CharField(_('sobrenome'), max_length=30, blank=True, null=True)
    is_staff = models.BooleanField(_('status de admin'), default=False, help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('ativo'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    is_host = models.BooleanField(_('anfitrião'), default=False, help_text=_('Permite o usuário adicionar imóveis na plataforma.'))
    date_joined = models.DateTimeField(_('data de registro'), default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
