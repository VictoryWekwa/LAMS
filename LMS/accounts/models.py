from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class myAccountManager(BaseUserManager):
    def create_user(self,email,username, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
                email = self.normalize_email(email),
                username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
               email=self.normalize_email(email),
               password = password,
               username = username,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user







class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name = "email", max_length = 60, unique = True)
    username        = models.CharField(max_length= 30, unique = True )
    first_name      = models.CharField(max_length = 50, verbose_name = "First Name")
    last_name       = models.CharField(max_length = 50, verbose_name = "Last Name")
    date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add= True)
    last_login      = models.DateTimeField(verbose_name= "last login", auto_now= True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default = True)
    is_staff        = models.BooleanField(default = False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'username' 
    
    REQUIRED_FIELDS = ['email']

    #how to use the manager 
    objects = myAccountManager()


    def __str__(self):
        return self.username

    def has_perm(self, perrm, obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
    
