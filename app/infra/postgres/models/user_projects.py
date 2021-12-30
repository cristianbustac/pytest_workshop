from tortoise.models import Model
from tortoise import fields


class UserProjects(Model):
    id = fields.IntField(pk=True)
    project = fields.ForeignKeyField('models.Project',related_name='project')
    user = fields.ForeignKeyField('models.UserIn', related_name='user')
    
    class Meta():
        unique_together =( ('project', 'user'))