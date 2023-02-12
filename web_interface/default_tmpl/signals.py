from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Default_Templates 

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

@receiver(post_save, sender=User)
def create_template(sender, instance, created, **kwargs):
    if created:
        Default_Templates.objects.create(Default_Templates=instance)
