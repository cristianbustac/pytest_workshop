from tortoise.models import Model
from tortoise import fields


class Project(Model):
    id = fields.IntField(pk=True)
    name_project = fields.TextField(null=False)
    start_date = fields.DateField(null=False)
    end_date = fields.DateField(null=False)
    backend_leader = fields.TextField(null=False)
    frontend_leader = fields.TextField(null=False)