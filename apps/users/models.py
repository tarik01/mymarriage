from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name='E-mail do Usuário',
        max_length=200,
        unique=True)
    
    is_active = models.BooleanField(
        verbose_name='Usuário Ativo',
        default=False)
    
    is_staff = models.BooleanField(
        verbose_name='Usuário da Equipe',
        default=False)
    
    is_superuser = models.BooleanField(
        verbose_name='Super Usuário',
        default=False)
    
    created_at = models.DateTimeField(
        verbose_name='Data de Cadastro',
        auto_now_add=True)

    updated_at = models.DateTimeField(
        verbose_name='Data de Atualização',
        auto_now=True,
        null=True,
        blank=True)
    
    USERNAME_FIELD = 'email'
    
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        return self.email   