Jupyter Contrib Core
====================

[![GitHub issues](https://img.shields.io/github/issues/jupyter-contrib/jupyter_contrib_core.svg?maxAge=3600)](https://github.com/jupyter-contrib/jupyter_contrib_core/issues) [![GitHub tag](https://img.shields.io/github/tag/jupyter-contrib/jupyter_contrib_core.svg?maxAge=3600)](https://github.com/jupyter-contrib/jupyter_contrib_core) [![Github All Releases](https://img.shields.io/github/downloads/jupyter-contrib/jupyter_contrib_core/total.svg?maxAge=3600)](https://github.com/jupyter-contrib/jupyter_contrib_core) [![PyPI](https://img.shields.io/pypi/v/jupyter_contrib_core.svg?maxAge=3600)](https://pypi.python.org/pypi/jupyter_contrib_core) [![PyPI](https://img.shields.io/pypi/dm/jupyter_contrib_core.svg?maxAge=3600)](https://pypi.python.org/pypi/jupyter_contrib_core)
<br/>
[![Travis-CI Build Status](https://img.shields.io/travis/Jupyter-contrib/jupyter_contrib_core.svg?maxAge=3600&label=Travis)](https://travis-ci.org/Jupyter-contrib/jupyter_contrib_core) [![Appveyor Build status](https://img.shields.io/appveyor/ci/jcb91/jupyter-contrib-core.svg?maxAge=3600&label=Appveyor)](https://ci.appveyor.com/project/jcb91/jupyter-contrib-core) [![Coveralls python test coverage](https://img.shields.io/coveralls/Jupyter-contrib/jupyter_contrib_core/master.svg?maxAge=3600&label=Coveralls)](https://coveralls.io/github/Jupyter-contrib/jupyter_contrib_core) [![Codecov python test coverage](https://img.shields.io/codecov/c/github/Jupyter-contrib/jupyter_contrib_core/master.svg?maxAge=3600&label=Codecov)](https://codecov.io/gh/Jupyter-contrib/jupyter_contrib_core)

Common utilities for jupyter-contrib projects. Includes:

-   providing a notebook-4.2-compatible nbextension API in order to
    smooth over differences in versions 4.0 and 4.1
-   common application components and cli scripts
-   utility classes and functions for use in tests


Changes
=======

0.3.0
-----

* Get `jupyter contrib` app subcommands from `pkg_resources` entrypoints
* Add `_maybe_copy` and `_should_copy` to nbextensions private API, since the
  `logger` keyword arg was only added after notebook 4.1
* Also patch `JUPYTER_RUNTIME_DIR` environment variable in
  `testing_utils.jupyter_env`

0.2.0
-----

Include almost-full 4.2 nbextensions public API

0.1.0
-----

Move raise_on_bad_version to testing_utils package.

0.0.1
-----

First public release!

