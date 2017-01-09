from arouse._dj.apps import AppConfig
from arouse._dj.db.backends.signals import connection_created
from arouse._dj.db.models import CharField, TextField
from arouse._dj.utils.translation import ugettext_lazy as _

from .lookups import SearchLookup, TrigramSimilar, Unaccent
from .signals import register_hstore_handler


class PostgresConfig(AppConfig):
    name = 'arouse._dj.contrib.postgres'
    verbose_name = _('PostgreSQL extensions')

    def ready(self):
        connection_created.connect(register_hstore_handler)
        CharField.register_lookup(Unaccent)
        TextField.register_lookup(Unaccent)
        CharField.register_lookup(SearchLookup)
        TextField.register_lookup(SearchLookup)
        CharField.register_lookup(TrigramSimilar)
        TextField.register_lookup(TrigramSimilar)
