from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class AccountUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': "El correo electrónico ya está registrado. Por favor, usa otro.",
        }
    )

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Title"
    )
    author = models.CharField(
        max_length=150,
        verbose_name="Author"
    )
    valuation = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10000),
        ],
        verbose_name="Valuation"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At"
    )
    
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        permissions = [
            ('development', 'Permiso como Desarrollador'),
            ('scrum_master', 'Permiso como Scrum Master'),
            ('product_owner', 'Permiso como Product Owner'),
        ]

    def __str__(self):
        return f"{self.title} - {self.author}"

