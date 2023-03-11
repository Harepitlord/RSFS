from rolepermissions.roles import AbstractUserRole

class Authority(AbstractUserRole):
    available_permissions={
        'view'
    }