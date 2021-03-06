"""Requirements specific to SQLAlchemy's own unit tests.


"""

from sqlalchemy import util
import sys
from sqlalchemy.testing.requirements import SuiteRequirements
from sqlalchemy.testing import exclusions
from sqlalchemy.testing.exclusions import \
     skip, \
     skip_if,\
     only_if,\
     only_on,\
     fails_on_everything_except,\
     fails_if,\
     succeeds_if,\
     SpecPredicate,\
     against

def no_support(db, reason):
    return SpecPredicate(db, description=reason)

def exclude(db, op, spec, description=None):
    return SpecPredicate(db, op, spec, description=description)

class DefaultRequirements(SuiteRequirements):
    @property
    def deferrable_or_no_constraints(self):
        """Target database must support derferable constraints."""

        return skip_if([
            no_support('firebird', 'not supported by database'),
            no_support('mysql', 'not supported by database'),
            no_support('mssql', 'not supported by database'),
            ])

    @property
    def named_constraints(self):
        """target database must support names for constraints."""

        return skip_if([
            no_support('sqlite', 'not supported by database'),
            ])

    @property
    def foreign_keys(self):
        """Target database must support foreign keys."""

        return skip_if(
                no_support('sqlite', 'not supported by database')
            )

    @property
    def unbounded_varchar(self):
        """Target database must support VARCHAR with no length"""

        return skip_if([
                "firebird", "oracle", "mysql"
            ], "not supported by database"
            )

    @property
    def boolean_col_expressions(self):
        """Target database must support boolean expressions as columns"""
        return skip_if([
            no_support('firebird', 'not supported by database'),
            no_support('oracle', 'not supported by database'),
            no_support('mssql', 'not supported by database'),
            no_support('sybase', 'not supported by database'),
            no_support('maxdb', 'FIXME: verify not supported by database'),
            no_support('informix', 'not supported by database'),
        ])

    @property
    def standalone_binds(self):
        """target database/driver supports bound parameters as column expressions
        without being in the context of a typed column.

        """
        return skip_if(["firebird", "mssql+mxodbc"],
                "not supported by driver")

    @property
    def identity(self):
        """Target database must support GENERATED AS IDENTITY or a facsimile.

        Includes GENERATED AS IDENTITY, AUTOINCREMENT, AUTO_INCREMENT, or other
        column DDL feature that fills in a DB-generated identifier at INSERT-time
        without requiring pre-execution of a SEQUENCE or other artifact.

        """
        return skip_if(["firebird", "oracle", "postgresql", "sybase"],
                "not supported by database"
            )

    @property
    def reflectable_autoincrement(self):
        """Target database must support tables that can automatically generate
        PKs assuming they were reflected.

        this is essentially all the DBs in "identity" plus Postgresql, which
        has SERIAL support.  FB and Oracle (and sybase?) require the Sequence to
        be explicitly added, including if the table was reflected.
        """
        return skip_if(["firebird", "oracle", "sybase"],
                "not supported by database"
            )

    @property
    def binary_comparisons(self):
        """target database/driver can allow BLOB/BINARY fields to be compared
        against a bound parameter value.
        """
        return skip_if(["oracle", "mssql"],
                "not supported by database/driver"
            )

    @property
    def independent_cursors(self):
        """Target must support simultaneous, independent database cursors
        on a single connection."""

        return skip_if(["mssql+pyodbc", "mssql+mxodbc"], "no driver support")

    @property
    def independent_connections(self):
        """Target must support simultaneous, independent database connections."""

        # This is also true of some configurations of UnixODBC and probably win32
        # ODBC as well.
        return skip_if([
                    no_support("sqlite",
                            "independent connections disabled "
                                "when :memory: connections are used"),
                    exclude("mssql", "<", (9, 0, 0),
                            "SQL Server 2005+ is required for "
                                "independent connections"
                        )
                    ]
                )

    @property
    def updateable_autoincrement_pks(self):
        """Target must support UPDATE on autoincrement/integer primary key."""

        return skip_if(["mssql", "sybase"],
                "IDENTITY columns can't be updated")

    @property
    def isolation_level(self):
        return only_on(
                    ('postgresql', 'sqlite', 'mysql'),
                    "DBAPI has no isolation level support"
                ).fails_on('postgresql+pypostgresql',
                          'pypostgresql bombs on multiple isolation level calls')

    @property
    def row_triggers(self):
        """Target must support standard statement-running EACH ROW triggers."""

        return skip_if([
            # no access to same table
            no_support('mysql', 'requires SUPER priv'),
            exclude('mysql', '<', (5, 0, 10), 'not supported by database'),

            # huh?  TODO: implement triggers for PG tests, remove this
            no_support('postgresql',
                    'PG triggers need to be implemented for tests'),
        ])

    @property
    def correlated_outer_joins(self):
        """Target must support an outer join to a subquery which
        correlates to the parent."""

        return skip_if("oracle", 'Raises "ORA-01799: a column may not be '
                    'outer-joined to a subquery"')

    @property
    def update_from(self):
        """Target must support UPDATE..FROM syntax"""

        return only_on(['postgresql', 'mssql', 'mysql'],
                "Backend does not support UPDATE..FROM")


    @property
    def update_where_target_in_subquery(self):
        """Target must support UPDATE where the same table is present in a
        subquery in the WHERE clause.

        This is an ANSI-standard syntax that apparently MySQL can't handle,
        such as:

        UPDATE documents SET flag=1 WHERE documents.title IN
            (SELECT max(documents.title) AS title
                FROM documents GROUP BY documents.user_id
            )
        """
        return fails_if('mysql', 'MySQL error 1093 "Cant specify target table '
                                        'for update in FROM clause"')

    @property
    def savepoints(self):
        """Target database must support savepoints."""

        return skip_if([
                    "sqlite",
                    "sybase",
                    ("mysql", "<", (5, 0, 3)),
                    ("informix", "<", (11, 55, "xC3"))
                    ], "savepoints not supported")


    @property
    def schemas(self):
        """Target database must support external schemas, and have one
        named 'test_schema'."""

        return skip_if([
                    "sqlite",
                    "firebird"
                ], "no schema support")


    @property
    def update_nowait(self):
        """Target database must support SELECT...FOR UPDATE NOWAIT"""
        return skip_if(["firebird", "mssql", "mysql", "sqlite", "sybase"],
                "no FOR UPDATE NOWAIT support"
            )

    @property
    def subqueries(self):
        """Target database must support subqueries."""

        return skip_if(exclude('mysql', '<', (4, 1, 1)), 'no subquery support')

    @property
    def intersect(self):
        """Target database must support INTERSECT or equivalent."""

        return fails_if([
                "firebird", "mysql", "sybase", "informix"
            ], 'no support for INTERSECT')

    @property
    def except_(self):
        """Target database must support EXCEPT or equivalent (i.e. MINUS)."""
        return fails_if([
                "firebird", "mysql", "sybase", "informix"
            ], 'no support for EXCEPT')

    @property
    def offset(self):
        """Target database must support some method of adding OFFSET or
        equivalent to a result set."""
        return fails_if([
                "sybase"
            ], 'no support for OFFSET or equivalent')

    @property
    def window_functions(self):
        return only_if([
                    "postgresql", "mssql", "oracle"
                ], "Backend does not support window functions")

    @property
    def two_phase_transactions(self):
        """Target database must support two-phase transactions."""

        return skip_if([
            no_support('firebird', 'no SA implementation'),
            no_support('maxdb', 'two-phase xact not supported by database'),
            no_support('mssql', 'two-phase xact not supported by drivers'),
            no_support('oracle', 'two-phase xact not implemented in SQLA/oracle'),
            no_support('drizzle', 'two-phase xact not supported by database'),
            no_support('sqlite', 'two-phase xact not supported by database'),
            no_support('sybase', 'two-phase xact not supported by drivers/SQLA'),
            no_support('postgresql+zxjdbc',
                    'FIXME: JDBC driver confuses the transaction state, may '
                       'need separate XA implementation'),
            exclude('mysql', '<', (5, 0, 3),
                        'two-phase xact not supported by database'),
            ])

    @property
    def views(self):
        """Target database must support VIEWs."""

        return skip_if("drizzle", "no VIEW support")

    @property
    def empty_strings_varchar(self):
        """target database can persist/return an empty string with a varchar."""

        return fails_if(["oracle"],
                        'oracle converts empty strings to a blank space')

    @property
    def empty_strings_text(self):
        """target database can persist/return an empty string with an
        unbounded text."""

        return exclusions.open()

    @property
    def unicode_data(self):
        return skip_if([
            no_support("sybase", "no unicode driver support")
            ])

    @property
    def unicode_connections(self):
        """Target driver must support some encoding of Unicode across the wire."""
        # TODO: expand to exclude MySQLdb versions w/ broken unicode
        return skip_if([
            exclude('mysql', '<', (4, 1, 1), 'no unicode connection support'),
            ])

    @property
    def unicode_ddl(self):
        """Target driver must support some encoding of Unicode across the wire."""
        # TODO: expand to exclude MySQLdb versions w/ broken unicode
        return skip_if([
            no_support('maxdb', 'database support flakey'),
            no_support('oracle', 'FIXME: no support in database?'),
            no_support('sybase', 'FIXME: guessing, needs confirmation'),
            no_support('mssql+pymssql', 'no FreeTDS support'),
            exclude('mysql', '<', (4, 1, 1), 'no unicode connection support'),
            ])

    @property
    def sane_rowcount(self):
        return skip_if(
            lambda: not self.db.dialect.supports_sane_rowcount,
            "driver doesn't support 'sane' rowcount"
        )

    @property
    def cextensions(self):
        return skip_if(
                lambda: not self._has_cextensions(), "C extensions not installed"
                )

    @property
    def emulated_lastrowid(self):
        """"target dialect retrieves cursor.lastrowid or an equivalent
        after an insert() construct executes.
        """
        return fails_on_everything_except('mysql+mysqldb', 'mysql+oursql',
                                      'sqlite+pysqlite', 'mysql+pymysql',
                                      'sybase', 'mssql+pyodbc', 'mssql+mxodbc')

    @property
    def implements_get_lastrowid(self):
        return skip_if([
            no_support('sybase', 'not supported by database'),
            ])

    @property
    def dbapi_lastrowid(self):
        """"target backend includes a 'lastrowid' accessor on the DBAPI
        cursor object.

        """
        return fails_on_everything_except('mysql+mysqldb', 'mysql+oursql',
                                       'sqlite+pysqlite', 'mysql+pymysql')

    @property
    def sane_multi_rowcount(self):
        return skip_if(
                    lambda: not self.db.dialect.supports_sane_multi_rowcount,
                    "driver doesn't support 'sane' multi row count"
                )

    @property
    def nullsordering(self):
        """Target backends that support nulls ordering."""
        return fails_on_everything_except('postgresql', 'oracle', 'firebird')

    @property
    def reflects_pk_names(self):
        """Target driver reflects the name of primary key constraints."""

        return fails_on_everything_except('postgresql', 'oracle', 'mssql',
                    'sybase')

    @property
    def datetime(self):
        """target dialect supports representation of Python
        datetime.datetime() objects."""

        return exclusions.open()

    @property
    def datetime_microseconds(self):
        """target dialect supports representation of Python
        datetime.datetime() with microsecond objects."""

        return skip_if(['mssql', 'mysql', 'firebird', '+zxjdbc',
                    'oracle', 'sybase'])

    @property
    def datetime_historic(self):
        """target dialect supports representation of Python
        datetime.datetime() objects with historic (pre 1900) values."""

        return succeeds_if(['sqlite', 'postgresql', 'firebird'])

    @property
    def date(self):
        """target dialect supports representation of Python
        datetime.date() objects."""

        return exclusions.open()

    @property
    def date_historic(self):
        """target dialect supports representation of Python
        datetime.datetime() objects with historic (pre 1900) values."""

        return succeeds_if(['sqlite', 'postgresql', 'firebird'])

    @property
    def time(self):
        """target dialect supports representation of Python
        datetime.time() objects."""

        return skip_if(['oracle'])

    @property
    def time_microseconds(self):
        """target dialect supports representation of Python
        datetime.time() with microsecond objects."""

        return skip_if(['mssql', 'mysql', 'firebird', '+zxjdbc',
                    'oracle', 'sybase'])

    @property
    def python2(self):
        return skip_if(
                lambda: sys.version_info >= (3,),
                "Python version 2.xx is required."
                )

    @property
    def python3(self):
        return skip_if(
                lambda: sys.version_info < (3,),
                "Python version 3.xx is required."
                )

    @property
    def python26(self):
        return skip_if(
                lambda: sys.version_info < (2, 6),
                "Python version 2.6 or greater is required"
            )

    @property
    def python25(self):
        return skip_if(
                lambda: sys.version_info < (2, 5),
                "Python version 2.5 or greater is required"
            )

    @property
    def cpython(self):
        return only_if(lambda: util.cpython,
               "cPython interpreter needed"
             )

    @property
    def predictable_gc(self):
        """target platform must remove all cycles unconditionally when
        gc.collect() is called, as well as clean out unreferenced subclasses.

        """
        return self.cpython

    @property
    def hstore(self):
        def check_hstore():
            if not against("postgresql"):
                return False
            try:
                self.db.execute("SELECT 'a=>1,a=>2'::hstore;")
                return True
            except:
                return False

        return only_if(check_hstore)

    @property
    def sqlite(self):
        return skip_if(lambda: not self._has_sqlite())

    @property
    def ad_hoc_engines(self):
        """Test environment must allow ad-hoc engine/connection creation.

        DBs that scale poorly for many connections, even when closed, i.e.
        Oracle, may use the "--low-connections" option which flags this requirement
        as not present.

        """
        return skip_if(lambda: self.config.options.low_connections)

    @property
    def skip_mysql_on_windows(self):
        """Catchall for a large variety of MySQL on Windows failures"""

        return skip_if(self._has_mysql_on_windows,
                "Not supported on MySQL + Windows"
            )

    @property
    def english_locale_on_postgresql(self):
        return skip_if(lambda: against('postgresql') \
                    and not self.db.scalar('SHOW LC_COLLATE').startswith('en'))

    @property
    def selectone(self):
        """target driver must support the literal statement 'select 1'"""
        return skip_if(["oracle", "firebird"], "non-standard SELECT scalar syntax")

    def _has_cextensions(self):
        try:
            from sqlalchemy import cresultproxy, cprocessors
            return True
        except ImportError:
            return False

    def _has_sqlite(self):
        from sqlalchemy import create_engine
        try:
            create_engine('sqlite://')
            return True
        except ImportError:
            return False

    def _has_mysql_on_windows(self):
        return against('mysql') and \
                self.db.dialect._detect_casing(self.db) == 1

    def _has_mysql_fully_case_sensitive(self):
        return against('mysql') and \
                self.db.dialect._detect_casing(self.db) == 0

