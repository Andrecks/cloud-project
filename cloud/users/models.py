from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=150, unique=True)
    wish = models.TextField(_('wish field'), blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_active = models.BooleanField(_('active'), default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email