from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.

class ZW_User(AbstractUser):
    stays_anonymous = models.BooleanField(default=False, verbose_name="Anoniem", blank=False, null=False)
    title = models.CharField(max_length=10, verbose_name="Aanhef", default="De heer", blank=False, null=False)

    def __str__(self):
        return self.title + " " +self.first_name + " " + self.last_name