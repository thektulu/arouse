from arouse._dj.db.models import Model


class ModelRegistry:
    def __init__(self, scanner):
        self._scanner = scanner
        self._included_registers = []
        self._self_models = {}
        self._models = {}
        self._ready = False

    def include(self, *registers):
        if self._ready:
            raise RuntimeError('Cannot include - register is in ready state')
        self._included_registers.extend(registers)

    def setup(self):
        if self._ready:
            return
        # TODO add some locking on readiness :)

        for register in self._included_registers:
            register.setup()
        self._self_setup()

    def _self_setup(self):
        self._scanner.scan()
        for model_name, schema in self._scanner.get_model_schemas():
            model_dict = {
                '__module__': schema.__module__
            }
            model = type(model_name, (schema, Model), model_dict)
            self._self_models[model_name] = model
        self._ready = True

    def lookup(self, model_name):
        model = self._models.get(model_name)
        if model is not None:
            return model

        model = self._self_models.get(model_name)
        if model is not None:
            return model

        for regster in self._included_registers:
            model = register.lookup(model_name)
            if model is not None:
                break

        return model


class ModelLookup:
    def __init__(self, registry):
        self._registry = registry

    def __getattr__(self, name):
        if name.startswith('_'):
            return object.__getattribute__(self, name)

        model = self._registry.lookup(name)
        if model is None:
            raise AttributeError(name)

        return model
