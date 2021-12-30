from tortoise.models import Model
from tortoise import fields


class RoleUsers(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.UserIn', related_name='users')
    role = fields.ForeignKeyField('models.Role', related_name='role')

    class Meta():
        unique_together =( ('user', 'role') )