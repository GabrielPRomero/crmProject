from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Lead(models.Model):
    first_name = models.CharField( max_length=20)
    last_name = models.CharField( max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    def __str__(self):
           return self.first_name
       
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_content')
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
       return self.user.email
   
   
def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)