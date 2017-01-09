from importlib import import_module

import venusian

from arouse.schema import Schema


def scanner_callback(scanner, name, schema):
    if not issubclass(schema, Schema):
        raise RuntimeError('Not a schema')

    if not schema.__module__.startswith(scanner.category):
        raise RuntimeError(
            'Can register to this scanner only inside "{}"'.format(
                scanner.category
            )
        )

    scanner.registry[name] = schema


class Scanner:
    def __init__(self, root_module):
        self.registry = {}
        self.root_module = root_module
        self.venusian_scanner = venusian.Scanner(
            registry=self.registry, category=self.root_module
        )

    def model(self, schema):
        venusian.attach(schema, scanner_callback, category=self.root_module)
        return schema

    def scan(self):
        try:
            root_module = import_module(self.root_module)
        except ImportError:
            return

        self.venusian_scanner.scan(
            root_module, categories=(self.root_module,)
        )

    def get_model_schemas(self):
        return self.registry.items()
