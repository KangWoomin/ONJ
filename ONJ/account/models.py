from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, birth, password=None, **extra):
        user = self.model(
            email = self.normalized_email('email'),
            birth = birth,
            **extra
        )
        user.set_password('password')
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None, **extra):
        extra.setdefault('birth','2000-01-01')
        extra.setdefault('is_admin', True)
        extra.setdefault('is_staff', True)

        user = self.create_user(
            email=email,
            password=password,
            **extra
        )
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    birth = models.DateField()
    nickname = models.CharField(verbose_name='nickname', max_length=80, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUESTED_FIELDS = ['birth']

    def __str__(self):
        return self.nickname
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin