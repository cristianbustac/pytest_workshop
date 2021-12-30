from tortoise.models import Model
from tortoise import fields


class UserOut(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField(null=False)
    lastname = fields.TextField(null=False)
    document_id = fields.IntField(null=False)
    address = fields.TextField(null=False)
    email = fields.CharField(max_length=10, unique=True, null=False)
    role_id = fields.IntField(null=False)


class UserIn(UserOut):
    password = fields.TextField(null=False)
    permission = fields.BooleanField(null=True)
