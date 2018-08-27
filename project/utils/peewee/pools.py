from peewee_async import PooledPostgresqlDatabase


def get_pool(name, user, password, host, port, max_conn=2):
    """Get database pool"""
    return PooledPostgresqlDatabase(
        name,
        max_connections=max_conn,
        user=user,
        password=password,
        host=host,
        port=port)
