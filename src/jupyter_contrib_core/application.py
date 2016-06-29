# coding: utf-8
"""
Common application classes for jupyter_contrib.

Including the root `jupyter-contrib` command.
"""

from __future__ import print_function

import sys

from jupyter_core.application import JupyterApp

from jupyter_contrib_core import __version__


class JupyterContribApp(JupyterApp):
    """Root level jupyter_contrib app."""

    name = 'jupyter contrib'
    version = __version__
    description = (
        'community-contributed spice for Jupyter Interactive Computing')

    def start(self):
        """Perform the App's actions as configured"""
        super(JupyterContribApp, self).start()

        # The above should have called a subcommand and raised NoStart; if we
        # get here, it didn't, so we should self.log.info a message.
        self.print_help()
        subcmds = ", ".join(sorted(self.subcommands))
        sys.exit("Please supply at least one subcommand: %s" % subcmds)

main = JupyterContribApp.launch_instance

if __name__ == '__main__':  # pragma: no cover
    main()
