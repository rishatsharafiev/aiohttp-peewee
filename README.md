# wp-bot

### Database
```
~$ sudo su - postgres

~$ createuser <PG_USER>
~$ createdb <PG_NAME>

~$ psql

postgres=# alter user <PG_USER> createdb;

postgres=# grant all privileges on database <PG_NAME> to <PG_USER>;
postgres=# alter user <PG_USER> with encrypted password '<PG_USER>';
```

### Migrations
```
# List migrations
pw_migrate list --directory <migrations_folder> --database postgresql://<username>:<password>@<host>:<port>/<db_name>

# Create migration
pw_migrate create <migration_name> --directory <migrations_folder> --database postgresql://<username>:<password>@<host>:<port>/<db_name>

# Create migration from models
pw_migrate create <migration_name> --auto <models> --directory <migrations_folder> --database postgresql://<username>:<password>@<host>:<port>/<db_name>

# Migrate
pw_migrate migrate --directory <migrations_folder> --database postgresql://<username>:<password>@<host>:<port>/<db_name>

# Rollback
pw_migrate rollback <migration_name> --directory <migrations_folder> --database postgresql://<username>:<password>@<host>:<port>/<db_name>

# <models> - project.apps.bot.models
# <migrations_folder> - project/apps/bot/migrations
# <migration_name> - initial, auto_20180123_1601, model_field, name the migrations based on feature eg implement_user_roles or make_employee_profile_editable
# postgresql://<username>:<password>@<host>:<port>/<db_name> - postgresql://wp_bot:wp_bot@localhost:5432/wp_bot
```