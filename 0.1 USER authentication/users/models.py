from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
#from .validation import *

class UserManager(BaseUserManager):
 def create_user(self, email, password, is_active, contact_number):
  if not email or not password:
   raise ValueError("EMAIL AND PASSWORD ARE MANDATORY")
  user = self.model(email=email, is_active=is_active, contact_number=contact_number)
  user.set_password(password)
  user.save(using=self._db)
  return user
 
 def create_superuser(self, email, password, is_active, contact_number):
  user = self.create_user(email=email, password=password, contact_number=contact_number, is_active=is_active)
  user.is_active = True
  user.is_admin = True
  user.is_staff = True
  user.is_superuser = True
  user.save(using=self._db)
  return user

class user_registration(AbstractBaseUser, PermissionsMixin):
  userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
  email = models.EmailField(unique=True, blank=False)
  contact_number = models.BigIntegerField(unique=True, blank=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['password', 'is_active', 'contact_number']

  class Meta:
    app_label = 'users'

class otp_session(models.Model):
  session_id = models.UUIDField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
  otp = models.IntegerField()
  phone = models.BigIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)