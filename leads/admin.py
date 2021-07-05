from django.contrib import admin

from django.contrib.auth import get_user_model
User = get_user_model()

from . import models
# Register your models here.
admin.site.register(User)
admin.site.register(models.Agent)
admin.site.register(models.lead)
admin.site.register(models.UserProfile)
admin.site.register(models.Category)
