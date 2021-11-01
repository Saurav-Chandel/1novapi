from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin ,BaseUserManager

from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
# Create your models here.

class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, email, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, first_name, password, **other_fields)

    def create_user(self, email, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)  
        user = self.model(email=email,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_('email addr'), unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=254, blank=True, null=True)
    otp = models.CharField(max_length=250, null=True, blank=True)
    # phone = models.IntegerField(max_length=12,unique=True,blank=True,null=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
 
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email


class Country(models.Model):
    country_code=models.CharField(max_length=50,null=True)
    name=models.CharField(max_length=100,verbose_name="Select Country")
    phonecode=models.IntegerField(max_length=100,null=True)

    def __str__(self):
        return self.name

class State1(models.Model):
    state_id=models.IntegerField(max_length=200)
    name=models.CharField(max_length=100)
    country_id=models.IntegerField(max_length=50)
    country_code=models.CharField(max_length=50)
    state_code=models.CharField(max_length=50,blank=True,null=True)
    # type=models.CharField(max_length=50,null=True,blank=True)
    latitude=models.DecimalField(max_digits=50,decimal_places=20,null=True)
    longitude=models.DecimalField(max_digits=50,decimal_places=20,null=True)

    def __str__(self):
        return self.name

class City(models.Model):
    
    name=models.CharField(max_length=100)
    state_id=models.IntegerField(max_length=100)
    state_code=models.CharField(max_length=100,null=True)
    country_id=models.IntegerField(max_length=100,null=True)
    country_code=models.CharField(max_length=100,null=True)
    latitude=models.DecimalField(max_digits=50,decimal_places=20,null=True)
    longitude=models.DecimalField(max_digits=50,decimal_places=20,null=True)
    wikiDataId=models.CharField(max_length=200,null=True)


    def __Str__(self):
        return self.name                



# email send signals
@receiver(post_save, sender=User)
def send_new_officer_notification_email(sender, instance, created, **kwargs):

    # if a new officer is created, compose and send the email
    if created:
        otp = instance.otp if instance.otp else "no otp given"
        Message = "Your One Time Passcode is {} to activate your account.".format(
                otp
        )
        from_email = settings.EMAIL_HOST_USER
        send_mail(
                "Email Varification<Don't Reply>",
                Message,
                from_email,
                [instance],
                fail_silently=False,
            ) 




POOL = 'PL'
GARDEN = 'GR'
PARKING = 'PK'

AMUNITIES_CHOICES = [
        (POOL, 'three'),
        (GARDEN, 'four'),
        (PARKING, 'available')
       ]
from django.db.models.signals import post_save, pre_delete,pre_save
from django.core.mail import EmailMultiAlternatives, send_mail
from django.dispatch import receiver

from django.core.mail import send_mail
# import base64
# import pyotp
from main import settings
           
    
class Post(models.Model):   
    user=models.ForeignKey(User,related_name = "user_post",on_delete=models.CASCADE)
    category=models.CharField(max_length=100,null=True,blank=True)
    bedroom=models.CharField(max_length=100,null=True,blank=True)
    kitchen=models.CharField(max_length=100,null=True,blank=True)
    area=models.CharField(max_length=100,null=True,blank=True)
    amunities=models.CharField(max_length=100,choices=AMUNITIES_CHOICES)

    def __str__(self):
        return self.category



class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline       


        


        



