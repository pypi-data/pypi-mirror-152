CherryPy-Psycopg2
=================

CherryPy-Psycopg2 is a simple CherryPy Tool to manage a
([thread-safe](https://www.psycopg.org/docs/pool.html#psycopg2.pool.ThreadedConnectionPool))
pool of database connections and make them available to handlers.

Import `cherrypy_psycopg2` to make the tool available in CherryPy's default toolbox.

The following configuration settings are understood:
  * `tools.psycopg2.minconn` - passed to the psycopg2 pool constructor
  * `tools.psycopg2.maxconn` - passed to the psycopg2 pool constructor
  * `tools.psycopg2.dsn` - passed to the psycopg2 pool constructor
  * `tools.psycopg2.cursor_factory` - passed to the psycopg2 connection's cursor() method

When the tool is enabled on a handler, it will collect a database connection
from the pool, expose a cursor as `cherrypy.request.psycopg2_cursor`,
execute the handler and then commit the transaction (if the handler was
successful or raised one of the
`cherrypy_psycopg2.COMMITTABLE_HANDLER_EXCEPTIONS`), or rollback the
transaction if the handler raised any other exception.

For example:

    class Root:
        @cherrypy.expose
        @cherrypy.tools.psycopg2()
        def index(self):
            cursor = cherrypy.request.psycopg2_cursor
            cursor.execute("SELECT now()")

            return cursor.fetchone()[0]
