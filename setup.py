#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name = 'etw',
    description = 'Edge Time Warp',

    author = 'Equinor',
    author_email = 'jegm@equinor.com',
    url = 'https://github.com/Equinor/etw',

    project_urls = {
        'Documentation': 'https://etw.readthedocs.io/',
        'Issue Tracker': 'https://github.com/Equinor/etw/issues',
    },
    keywords = [
    ],

    license = 'GNU Lesser General Public License v3',

    packages = [
        'etw',
    ],
    platforms = 'any',

    install_requires = [
    ],

    setup_requires = [
        'setuptools >=28',
        'setuptools_scm',
        'pytest-runner'
    ],

    tests_require = [
        'pytest',
    ],



    use_scm_version = {
        'write_to': 'etw/version.py',
    },
)
