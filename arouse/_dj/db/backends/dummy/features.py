from arouse._dj.db.backends.base.features import BaseDatabaseFeatures


class DummyDatabaseFeatures(BaseDatabaseFeatures):
    supports_transactions = False
