"""
A helper class to run migrations using a series of SQL files.
"""

import atexit
import logging
import os

from kinto.core.utils import sqlalchemy as sa


logger = logging.getLogger(__name__)


class MigratorMixin:
    """Mixin to allow the running of migrations.

    Your class must provide a `client` attribute (a PostgreSQLClient),
    as well as override some class attributes.
    """

    """Name of this migrator (e.g. "storage"). Override this."""
    name = None

    """The current "newest" schema version. Override this."""
    schema_version = None

    """The file to find the current "newest" schema in. Override this."""
    schema_file = None

    """The directory to find migration files in.

    Migrations should each be a file named migration_nnn_mmm.sql, where mmm = nnn + 1.
    """
    migrations_directory = None

    ### INSTRUMENTATION DATA STRUCTURE ###
    coverage_data_create_schema = {
    "branch 1": 0, ##if not dry_run
    "branch 2": 0, ##implicit else
    }

    def get_installed_version(self):
        """Return current version of schema or None if none found.

        Override this.

        This may be called several times during a single migration.
        """
        raise NotImplementedError("method not overridden")  # pragma: no cover

    def create_or_migrate_schema(self, dry_run=False):
        """Either create or migrate the schema, as needed."""
        version = self.get_installed_version()
        if not version:
            self.create_schema(dry_run)
            return

        logger.info(f"Detected PostgreSQL {self.name} schema version {version}.")
        if version == self.schema_version:
            logger.info(f"PostgreSQL {self.name} schema is up-to-date.")
            return

        self.migrate_schema(version, dry_run)

    ### SELECTED FUNCTION ###
    def create_schema(self, dry_run):
        """Actually create the schema from scratch using self.schema_file.

        You can override this if you want to add additional sanity checks.
        """
        logger.info(
            f"Create PostgreSQL {self.name} schema at version {self.schema_version} from {self.schema_file}."
        )
        if not dry_run:
            ## BRANCH 1 ##
            MigratorMixin.coverage_data_create_schema["branch 1"] += 1
            self._execute_sql_file(self.schema_file)
            logger.info(f"Created PostgreSQL {self.name} schema (version {self.schema_version}).")
        else:
            ## BRANCH 2 ##
            MigratorMixin.coverage_data_create_schema["branch 2"] += 1

    def migrate_schema(self, start_version, dry_run):
        migrations = [(v, v + 1) for v in range(start_version, self.schema_version)]
        for migration in migrations:
            expected = migration[0]
            current = self.get_installed_version()
            error_msg = f"PostgreSQL {self.name} schema: Expected version {expected}. Found version {current}."
            if not dry_run and expected != current:
                raise AssertionError(error_msg)

            logger.info(
                f"Migrate PostgreSQL {self.name} schema from version {migration[0]} to {migration[1]}."
            )
            filename = "migration_{0:03d}_{1:03d}.sql".format(*migration)
            filepath = os.path.join(self.migrations_directory, filename)
            logger.info(f"Execute PostgreSQL {self.name} migration from {filepath}")
            if not dry_run:
                self._execute_sql_file(filepath)
        logger.info(
            f"PostgreSQL {self.name} schema migration {'simulated' if dry_run else 'done'}"
        )

    def _execute_sql_file(self, filepath):
        """Helper method to execute the SQL in a file."""
        with open(filepath) as f:
            schema = f.read()
        # Since called outside request, force commit.
        with self.client.connect(force_commit=True) as conn:
            conn.execute(sa.text(schema))

    def print_coverage_data_create_schema():
        print("Branch Coverage Report for function create_schema:")
        print(f"Number of Branches: {len(MigratorMixin.coverage_data_create_schema)}")
        total_executed = sum(1 for count in MigratorMixin.coverage_data_create_schema.values() if count > 0)
        for branch, count in MigratorMixin.coverage_data_create_schema.items():
            print(f"{branch}: executed {count} time(s)")
        coverage_percentage = (total_executed / len(MigratorMixin.coverage_data_create_schema)) * 100
        print(f"Total Coverage: {coverage_percentage:.2f}% \n")


    atexit.register(print_coverage_data_create_schema)