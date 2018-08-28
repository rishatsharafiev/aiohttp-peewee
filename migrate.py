from project import settings

from peewee_migrate.cli import get_router

# TODO: write migrations for all apps migrate/rollback
# TODO: move to migration folder or utils

db_data = {
    'db_name': settings.PG_NAME,
    'username': settings.PG_USER,
    'password': settings.PG_PASSWORD,
    'host': settings.PG_HOST,
    'port': settings.PG_PORT,
}

db = 'postgresql://{username}:{password}@{host}:{port}/{db_name}'.format(**db_data)

directory = settings.BASE_PATH / 'apps' / 'migrations'


def migrate(name=None, database=None, directory=None, verbose=None, fake=False):
    """Migrate database."""
    router = get_router(directory, database, verbose)
    migrations = router.run(name, fake=fake)
    if migrations:
        print('Migrations completed: %s' % ', '.join(migrations))


migrate(database=db, directory=directory, verbose=True)
