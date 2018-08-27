from peewee_async import Manager


def get_manager(pool, loop):
    """Get database manager"""
    manager = Manager(pool, loop=loop)
    manager.database.allow_sync = False
    return manager
