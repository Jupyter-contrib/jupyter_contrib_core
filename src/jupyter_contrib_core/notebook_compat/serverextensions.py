# -*- coding: utf-8 -*-
"""Shim providing notebook.serverextensions stuff for pre 4.2 versions."""

try:  # notebook >= 4.2
    from notebook.serverextensions import (
        ToggleServerExtensionApp, toggle_serverextension_python,
    )
except ImportError:  # notebook <4.2
    from ._compat.serverextensions import (
        ToggleServerExtensionApp, toggle_serverextension_python,
    )

try:
    from notebook.extensions import ArgumentConflict  # notebook >= 5.0
except ImportError:
    try:
        from notebook.serverextensions import ArgumentConflict  # notebook 4.2.x
    except ImportError:
        from ._compat.serverextensions import ArgumentConflict  # notebook < 4.2


__all__ = [
    'ArgumentConflict', 'ToggleServerExtensionApp',
    'toggle_serverextension_python',
]
