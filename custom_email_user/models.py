from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.core.validators import EmailValidator
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given:
        email, password
        """
        existing_email = self.model.filter(
            email=email
        ).first()

        if existing_email:
            raise Exception('This email is already assigned to another User')

        user = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username', '')
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        """
        Creates and saves a Superuser with the given:
        email, password
        """
        existing_email = self.model.objects.filter(
            email=email
        ).first()

        if existing_email:
            raise Exception('This email is already assigned to another User')

        user = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username', '')
        )

        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        error_messages={
            'unique': "A user with that email already exists.",
        },
        help_text="Required. 150 characters or fewer.",
        max_length=150,
        unique=True,
        validators=[EmailValidator],
    )
    username = models.CharField(
        verbose_name="username",
        max_length=150,
        blank=True,
        help_text="150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[UnicodeUsernameValidator]
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True
