from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact_Us(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    body = models.TextField()
    contact_reason = models.CharField(max_length=200)
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-sent_on"]  # Order by sent date in descending order (most recent first)

    def __str__(self):
        return f"Contact Us from {self.first_name} {self.last_name} - Reason: {self.contact_reason}"