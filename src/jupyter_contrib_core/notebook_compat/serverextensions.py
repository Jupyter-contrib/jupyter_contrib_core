# -*- coding: utf-8 -*-
"""Shim providing notebook.serverextensions stuff for pre 4.2 versions."""

try:
    from notebook.serverextensions import (
        ToggleServerExtensionApp, toggle_serverextension_python,
    )
    from notebook.extensions import ArgumentConflict
except ImportError:
    from ._compat.serverextensions import (
        ArgumentConflict, ToggleServerExtensionApp,
        toggle_serverextension_python,
    )

__all__ = [
    'ArgumentConflict', 'ToggleServerExtensionApp',
    'toggle_serverextension_python',
]
