from django.contrib.auth.models import Group

class UserGroups:
    authority = 1
    logistics = 2
    shipper = 3

    ROLES = (
        (authority, "Authority"),
        (logistics, "Logistics"),
        (shipper, "Shipper")
    )

    ROLES_Map = (
        ("Authority", authority),
        ("Logistics", logistics),
        ("Shipper", shipper)
    )

    def get_permission_group(self, role: int):
        if role == self.authority:
            return Group.objects.get_or_create('Authority')

        if role == self.logistics:
            return Group.objects.get_or_create('Logistics')

        if role == self.shipper:
            return Group.objects.get_or_create('Shipper')
