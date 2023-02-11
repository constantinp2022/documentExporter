from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#import for Statistic
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from statistic.models import Statistic

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        #Statistic
        global stat
        number_of_users = User.objects.all().count();
        number_of_templates = -1
        number_of_documents = -1
        Statistic.objects.update_or_create(id=1, defaults={"number_of_users":number_of_users ,"number_of_templates":number_of_templates ,"number_of_documents":number_of_documents })


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save(force_insert=False)