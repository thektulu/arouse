import os
import inspect

from arouse.scanner import Scanner
from arouse.registry import ModelLookup, ModelRegistry

class Api:
    def __init__(self, scanner, registry):
        self.scanner = scanner
        self.registry = registry


def install(schema_root='schema'):
    l = inspect.getouterframes(inspect.currentframe())
    module_frame = l[1].frame
    module_locals = module_frame.f_locals

    root_module = '{}.{}'.format(module_locals['__package__'], schema_root)

    scanner = Scanner(root_module)
    registry = ModelRegistry(scanner)

    module_locals['api'] = Api(scanner, registry)
    module_locals['model'] = scanner.model
    module_locals['models'] = ModelLookup(registry)
    module_locals['setup'] = registry.setup
