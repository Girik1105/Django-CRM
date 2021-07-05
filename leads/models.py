from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
# Create your models here.

from phonenumber_field.modelfields import PhoneNumberField

#Abstarct user lets us make our owncustom user model
class User(AbstractUser):
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

    organisation_name = models.CharField(max_length=100, blank=True, null=True)

    phone_number = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    profile_picture = models.ImageField(blank=True, upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.jpg')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username


class lead(models.Model):
    agent = models.ForeignKey(Agent, null=True, related_name="leads", blank=True, on_delete=models.SET_NULL)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)

    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    address = models.TextField()
    profile_picture = models.ImageField(blank=True, upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.jpg')

    SOURCE_CHOICES = (
    ('', 'Select the Source'),
    ('Social Media', 'Social Media'),
    ('NewsLetter', 'Newsletter'),
    ('Ads', 'Advertisements'),
    ('Friend_Family', 'Friend or Family'),
    ('Other', 'Other')
    )
    source = models.CharField(choices=SOURCE_CHOICES, max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)
