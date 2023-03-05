from django.contrib.auth.models import BaseUserManager, Group
from django.utils import timezone
from .models import User


class UserGroups:
    Authority, created1 = Group.objects.get_or_create(name="Authority")
    Logistics, created2 = Group.objects.get_or_create(name="Logistics")
    Shipper, created3 = Group.objects.get_or_create(name="Shipper")

    ROLES_Map = (
        ("Authority", Authority),
        ("Logistics", Logistics),
        ("Shipper", Shipper)
    )
    ROLES = (
        "Authority", "Logistics", "Shipper"
    )

    def get_permission_group(self, role: int):
        if role == User.Authority:
            return self.Authority

        if role == User.Logistics:
            return self.Logistics

        if role == User.Shipper:
            return self.Shipper


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.groups.add(UserGroups().get_permission_group(role=extra_fields['role']))
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user
