# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .messages import (
    CRITICAL, DEBUG, ERROR, INFO, WARNING, CheckMessage, Critical, Debug,
    Error, Info, Warning,
)
from .registry import Tags, register, run_checks, tag_exists

# Import these to force registration of checks
import arouse._dj.core.checks.caches  # NOQA isort:skip
import arouse._dj.core.checks.database  # NOQA isort:skip
import arouse._dj.core.checks.model_checks  # NOQA isort:skip


__all__ = [
    'CheckMessage',
    'Debug', 'Info', 'Warning', 'Error', 'Critical',
    'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL',
    'register', 'run_checks', 'tag_exists', 'Tags',
]
