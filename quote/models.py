from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    CATEGORY = (
        (0, "Uncategorized"),
        (1, "Stress"),
        (2, "Shame"),
        (3, "Grief"),
        (4, "Self-worth"),
    )

class Notes(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=100, default='anonymous')
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    category = models.IntegerField(choices=CATEGORY, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    # def __str__(self):
    #     return self.name