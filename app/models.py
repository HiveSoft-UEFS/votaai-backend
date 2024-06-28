from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, cpf, email, name, lname, username, status, role, password=None, **extra_fields):
        if not email:
            raise ValueError('O email precisa ser fornecido')
        email = self.normalize_email(email)
        user = self.model(
            cpf=cpf,
            email=email,
            name=name,
            lname=lname,
            username=username,
            status=status,
            role=role,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, email, name, lname, username, status, role, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(cpf, email, name, lname, username, status, role, password, **extra_fields)

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    username = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=255, choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('BANNED', 'Banned')], default='ACTIVE')
    role = models.CharField(max_length=255, choices=[('MODERATOR', 'Moderator'), ('USER', 'User')], default='USER')
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['cpf', 'email', 'name', 'lname', 'status', 'role']

    def __str__(self):
        return self.username
