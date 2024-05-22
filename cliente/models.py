from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Usuarios precisam ter um email!')
        if not username:
            raise ValueError('Usuarios precisam ter um nome!')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    numero = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    empenho = models.FileField(upload_to='empenhos/', max_length=500)
    nfe = models.FileField(upload_to='notas/', max_length=500, default='0', blank=True)
    n_nfe = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)
    valor = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    def delete(self, *args, **kwargs):
        self.empenho.delete()
        self.nfe.delete()
        super().delete(*args, **kwargs)