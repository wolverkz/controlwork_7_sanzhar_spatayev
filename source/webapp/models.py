from django.db import models
from django.utils import timezone


# Create your models here.
class Guestbook(models.Model):
    STATUS = [
        ('active', 'Active'),
        ('blocked', 'Blocked')
    ]

    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Entry name')
    email = models.EmailField(max_length=40, null=False, blank=False, verbose_name='Entry email')
    desc = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Entry description')
    is_deleted = models.BooleanField(null=False, blank=False, default=False, verbose_name='Deletion status')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date updated at')
    status = models.CharField(max_length=10, choices=STATUS, default='active', verbose_name='Status of an entry')
    deleted_at = models.DateTimeField(null=True, default=None, verbose_name='Date when deleted')


    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()