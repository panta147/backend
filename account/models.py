import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have an Email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile = models.ImageField(upload_to="profile", null=True)
    date = models.DateField(null=True)
    email = models.EmailField(
        max_length=255, unique=True, verbose_name="Email Address")
    phone = models.CharField(max_length=20, default="", null=True)
    companyName = models.CharField(max_length=20, default="", null=True)
    companyType = models.CharField(max_length=20, default="", null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    userType = models.BooleanField(default=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'address', 'date', 'phone']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name_plural = "USER"

    def __str__(self):
        return f'{self.first_name}'

User = get_user_model()