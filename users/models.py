from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class BookingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
class Organization(models.Model):
    choice = models.CharField(max_length=100)

    objects = BookingManager()

    def __str__(self):
        return f"{self.choice}"

class PreferredContact(models.Model):
    choice = models.CharField(max_length=100)

    objects = BookingManager()

    def __str__(self):
        return f"{self.choice}"

class User(AbstractUser):
    is_member = models.BooleanField(default=False)
    mobile = models.CharField(max_length=30)
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL)
    domain = models.CharField(max_length=50)

class MembershipPlan(models.Model):
    price = models.IntegerField()
    time_period = models.CharField(max_length=50)

class Member(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    plan = models.ForeignKey(MembershipPlan, null=True, blank=True, on_delete=models.SET_NULL)