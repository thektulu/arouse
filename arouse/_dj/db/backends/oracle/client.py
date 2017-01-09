import subprocess

from arouse._dj.db.backends.base.client import BaseDatabaseClient


class DatabaseClient(BaseDatabaseClient):
    executable_name = 'sqlplus'

    def runshell(self):
        conn_string = self.connection._connect_string()
        args = [self.executable_name, "-L", conn_string]
        subprocess.call(args)
