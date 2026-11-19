from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_instructor = models.BooleanField(default=False) # sobreescrobimos al usuario predeterminado de django agregandole este campo

    def __str__(self):
        return self.get_full_name() or self.username
    