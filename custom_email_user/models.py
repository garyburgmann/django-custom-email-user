import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser as BaseAbstractUser
from django.utils.translation import gettext_lazy as _


class AbstractUser(BaseAbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True,
        error_messages={
            'unique': _('A user with that email already exists.'),
        },
    )

    class Meta:
        abstract = True


# class User(AbstractUser):
#     pass
