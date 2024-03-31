# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password

class UsersTbl(AbstractUser):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    username = models.CharField(max_length=150, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=128, blank=False)  # You should consider hashing the password
    
    # Additional fields if needed
    
    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.set_password(self.password)
        super().save(*args, **kwargs)
    
    def set_password(self, raw_password):
        """
        Sets the user's password to the given raw password, hashing it for security.
        """
        self.password = make_password(raw_password)

# Model for storing message
class Message(models.Model):
    from_user = models.ForeignKey(UsersTbl, on_delete=models.PROTECT, default=None, related_name="from_user")
    to_user = models.ForeignKey(UsersTbl, on_delete=models.PROTECT, default=None, related_name="to_user")
    message = models.TextField()
    created_date = models.DateField(null=True)
    created_time = models.TimeField(null=True)
    message_seen_status = models.BooleanField(null=False, default=False)