#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup script for jupyter_contrib_core."""

from __future__ import print_function

import os
from glob import glob

from setuptools import find_packages, setup


def main():

    setup(
        name='jupyter_contrib_core',
        description='Common utilities for jupyter-contrib projects.',
        long_description="""
Common utilities for jupyter-contrib projects. Includes:

-   providing a notebook-4.2-compatible nbextension API in order to
    smooth over differences in versions 4.0 and 4.1
-   common application components and cli scripts
-   utility classes and functions for use in tests
""",
        version='0.3.0',
        author='jcb91, jupyter-contrib developers',
        author_email='joshuacookebarnes@gmail.com',
        url=('https://github.com/'
             'jupyter-contrib/jupyter_contrib_core'),
        download_url=('https://github.com/'
                      'jupyter-contrib/jupyter_contrib_core/'
                      'tarball/0.3.0'),
        keywords=['Jupyter', 'notebook'],
        license='BSD 3-clause',
        platforms=['any'],
        packages=find_packages('src'),
        package_dir={'': 'src'},
        include_package_data=True,
        py_modules=[
            os.path.splitext(os.path.basename(path))[0]
            for path in glob('src/*.py')
        ],
        install_requires=[
            'jupyter_core',
            'notebook >=4.0',
            'setuptools',
            'traitlets',
            'tornado',
        ],
        extras_require={
            'testing_utils': [
                'nose',
            ],
            'testing_utils:python_version == "2.7"': [
                'mock',
            ],
        },
        # so far zip-safe as we're pure python
        zip_safe=True,
        entry_points={
            'console_scripts': [
                'jupyter-contrib = jupyter_contrib_core.application:main',  # noqa
            ],
        },
        scripts=[os.path.join('scripts', p) for p in [
            'jupyter-contrib',
        ]],
        classifiers=[
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: JavaScript',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Topic :: Utilities',
        ],
    )

if __name__ == '__main__':
    main()
