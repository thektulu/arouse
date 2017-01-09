from __future__ import unicode_literals

from arouse._dj.utils.version import get_version

VERSION = (1, 10, 6, 'alpha', 0)

__version__ = get_version(VERSION)


def setup(set_prefix=True):
    """
    Configure the settings (this happens as a side effect of accessing the
    first setting), configure logging and populate the app registry.
    Set the thread-local urlresolvers script prefix if `set_prefix` is True.
    """
    from arouse._dj.apps import apps
    from arouse._dj.conf import settings
    from arouse._dj.utils.encoding import force_text

    apps.populate(settings.INSTALLED_APPS)
