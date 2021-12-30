from tortoise.models import Model
from tortoise import fields


class Role(Model):
    id = fields.IntField(pk=True)
    name_role = fields.TextField(null=False)
    description = fields.TextField(null=False)
