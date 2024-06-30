from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, cpf, email, name, lname, username, status, role, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            cpf=cpf,
            email=self.normalize_email(email),
            name=name,
            lname=lname,
            username=username,
            status=status,
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, email, name, lname, username, status, role, password=None):
        user = self.create_user(
            cpf=cpf,
            email=email,
            name=name,
            lname=lname,
            username=username,
            status=status,
            role=role,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    username = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=255, choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('BANNED', 'Banned')])
    role = models.CharField(max_length=255, choices=[('MODERATOR', 'Moderator'), ('USER', 'User')])
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['cpf', 'email', 'name', 'lname', 'status', 'role']

    def __str__(self):
        return self.username