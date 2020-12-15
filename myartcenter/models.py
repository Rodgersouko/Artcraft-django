from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

# Create your models here.
# class Artcenter(models.Model):
#      title = models.CharField(max_length=35)
#      desc = models.CharField(max_length=250)

#signal for sending email.
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(
        reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have email address')
        if not username:
            raise ValueError('Users must have username')
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
  
class User(AbstractBaseUser):
    email       = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username    = models.CharField(max_length=30, unique=False)
    date_joined = models.DateTimeField(verbose_name="date-joined", auto_now_add=True)
    last_login   = models.DateTimeField(verbose_name="last-login", auto_now=True)
    is_admin     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()
    
    def __str_(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    # email = models.EmailField(verbose_name="email", max_length=60)

    def __str_(self):
        return self.album_title + '_' + self.artist



class Art(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    art_type = models.CharField(max_length=100)
    art_title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='downloads')
    

