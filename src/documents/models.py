from django.conf import settings
from django.db import models
from django.utils import timezone


User = settings.AUTH_USER_MODEL # 'auth.User'
# Create your models here.

class Document(models.Model):
    '''Document that will store parameters that the ai agent will have access to'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="title")
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    active_at = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({'Active' if self.active else 'Inactive'})"

    def save(self, *args, **kwargs):
        '''Change the field based on other fields behavior'''
        if self.active and self.active_at is None:
            self.active_at = timezone.now()
        else:
            self.active_at = None
        super().save(*args, **kwargs)


