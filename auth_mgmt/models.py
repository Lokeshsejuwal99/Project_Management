# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, UserManager, PermissionsMixin
# from django.utils import timezone
# # Create your models here.


# class UserManager(models.Model):
#  '''This is custom user manager'''

#  def create_user(self, email, password, **extra_fields):
#   if not email:
#    raise ValueError("Email is a required field.")
#   email = self.normalize_email(email)
#   extra_fields.setdefault("is_staff", False)
#   extra_fields.setdefault("is_superuser", False)
#   user = self.model(email=email, **extra_fields)
#   user.set_password(password)
#   user.save(using=self._db)
#   return user
 
#  def create_superuser(self, email, password, **extra_fields):
#   '''This is custom superuser'''

#   if not email:
#    raise ValueError("Email is a required field")
#   extra_fields.setdefault("is_staff", True)
#   extra_fields.setdefault("is_superuser", True)
#   extra_fields.setdefault("is_active", True)
#   email = self.normalize_email(email)
#   user = self.model(email=email, **extra_fields)
#   user.set_password(password)
#   user.save(using=self._db)
#   return user
 

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#  '''This is my custom MyUser subclass of AbstractBaseUser'''

#  email = models.EmailField(max_length=254, unique=True)
#  recovery_code = models.TextField()
#  mfa_enabled = models.BooleanField(default=False)
#  otp = models.CharField(max_length=6, blank=True, null=True)
#  is_active = models.BooleanField(default=True)
#  is_superuser = models.BooleanField(default=False)
#  date_joined = models.DateTimeField(default=timezone.now)
#  last_update = models.DateTimeField(auto_now=True)

#  USERNAME_FIELD = "email"
#  objects = UserManager()

#  def __str__(self):
#   return self.email
 