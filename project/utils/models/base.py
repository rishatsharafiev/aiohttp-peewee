import peewee

from project.settings import pool


class Base(peewee.Model):
    """Base db model"""

    uid = peewee.PrimaryKeyField(unique=True, index=True)

    # gid, uid, created_at, updated_at, is_deleted

    class Meta:
        database = pool
        order_by = ('-uid',)
