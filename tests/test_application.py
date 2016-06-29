# -*- coding: utf-8 -*-
"""Tests for the main app."""

from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

import logging
from unittest import TestCase

import nose.tools as nt
from traitlets.tests.utils import check_help_all_output, check_help_output

from jupyter_contrib_core.application import main as main_app
from jupyter_contrib_core.application import JupyterContribApp
from jupyter_contrib_core.testing_utils import (
    get_logger, patch_traitlets_app_logs,
)
from jupyter_contrib_core.testing_utils.jupyter_env import patch_jupyter_dirs

app_classes = [JupyterContribApp]


def reset_app_class(app_class):
    """Reset all app traits and clear the instance."""
    if app_class._instance is None:
        return
    for name, traitlet in app_class._instance.traits().items():
        if isinstance(traitlet.this_class, JupyterContribApp):
            setattr(app_class._instance, name, traitlet.default_value)
    app_class.clear_instance()


class AppTest(TestCase):
    """Tests for the main app."""

    @classmethod
    def setup_class(cls):
        cls.log = cls.log = get_logger(cls.__name__)
        cls.log.handlers = []
        cls.log.propagate = True

    def setUp(self):
        """Set up test fixtures for each test."""
        (jupyter_patches, self.jupyter_dirs,
         remove_jupyter_dirs) = patch_jupyter_dirs()
        for ptch in jupyter_patches:
            ptch.start()
            self.addCleanup(ptch.stop)
        self.addCleanup(remove_jupyter_dirs)

        for klass in app_classes:
            patch_traitlets_app_logs(klass)
            klass.log_level.default_value = logging.DEBUG

    def test_00_help_output(self):
        """Check that app help works."""
        app_module = 'jupyter_contrib_core.application'
        check_help_output(app_module, [])
        check_help_all_output(app_module, [])
        # sys.exit should be called if no argv specified
        with nt.assert_raises(SystemExit):
            main_app([])
