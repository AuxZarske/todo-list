from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Se define un nuevo modelo de usuario partiendo de AbstracUser, quitando el username,
    y se agregan los campos "country" y "description"
    """
    username = None
    email = models.EmailField(_("email address"), unique=True)
    country = models.CharField(max_length=40, blank=True)
    description = models.CharField(max_length=255, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email