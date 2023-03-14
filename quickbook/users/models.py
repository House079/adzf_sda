from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


CATEGORIS = (
        ('F','Fryzjerka'),
        ('R', 'Recepcjonistka'),
        ('S','Superviser'),
    )



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=256)
    position = models.CharField(max_length=20, choices=CATEGORIS, default='S')
    # salon = models.ForeignKey(<FK TO SALON>, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Tworzy profil dla karzdego urzytjownika jak tworzysz urzytkownika automatycznie jest tworzony profil z GOOGLE"""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Zapisuje stworzony profil do bazy danych"""
    instance.profile.save()



