from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed  #here's a signals
from django.db.models.signals import post_save, pre_delete,pre_save
# from django.contrib.auth.models import User  #here user ia s sender
from django.dispatch import receiver
from .models import User  # user is a sender.

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("***************")
    print("logged in signal")
    print("sender:", sender)
    print("request:", request)
    print("User:", user)
    # print("User:", user.password) #returns a password.
    print(f'kwargs:{kwargs}')
# user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out, sender=User)
def logged_out(sender, request, user, **kwargs):
    print("***************")
    print("logged out signal")
    print("sender:", sender)
    print("request:", request)
    print("User:", user)
    print(f'kwargs:{kwargs}') 
# user_logged_out.connect(loged_out,sender=User)

@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
    print("***************")
    print("login failed signal")
    print("sender:", sender)
    print("credentials:", credentials)
    print("request:", request)
    # print("User:", user)
    print(f'kwargs:{kwargs}') 







   



# post_save.connect(email_sender, sender=User)          