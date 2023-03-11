from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
from .modelHelper import UserGroups


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Email", max_length=254, unique=True)
    name = models.CharField(verbose_name="Name", max_length=254, null=True, blank=True)
    country = models.CharField(verbose_name="Country", max_length=25, null=False, )
    phone_no = models.CharField(verbose_name="Phone:", max_length=12, null=False, )
    role = models.PositiveSmallIntegerField(verbose_name="Role", choices=UserGroups.ROLES)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    PASSWORD_FIELD = 'password'
    REQUIRED_FIELDS = ['country', 'name', 'phone_no', 'password']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % self.pk
