# -*- coding: utf-8 -*-
"""
    Setup package
    ~~~~~~~~~~~~~~~~~~~~

    Setuptools/distutils commands to package installation.

    :author: Marco Lovato
    :contact: maglovato@gmail.com
    :license: Other/Proprietary, see LICENSE for details.
"""
# pylint: HOOK-IGNORED

import os
from setuptools import Command, setup, find_packages
import string
import re
from distutils.version import StrictVersion
from subprocess import Popen, PIPE, STDOUT, call
import subprocess

# Hack to silence atexit traceback in newer python versions
try:
    import multiprocessing
except ImportError:
    pass

project_name = 'packagesample'
__version__ = __import__(project_name).__version__
__author__ = __import__(project_name).__author__
__description__ = __import__(project_name).__description__


def cmd_output(args, **kwds):
    kwds.setdefault("stdout", subprocess.PIPE)
    kwds.setdefault("stderr", subprocess.STDOUT)
    p = subprocess.Popen(args, **kwds)
    return p.communicate()[0]


def version_tuple(version):
    return tuple([int(num) for num in version.split('.')])


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        pass
    return ''


CLASSIFIERS = [
    'Environment :: Library',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Operating System :: OS Independent',
    'Topic :: Internet :: WWW/HTTP',
]

setup(
    author=__author__,
    author_email='maglovato@gmail.com',
    classifiers=CLASSIFIERS,
    description=__description__,
    entry_points={
        'console_scripts': [
            project_name + '_app = ' + project_name + '.start:main'
        ]
    },
    include_package_data=True,
    install_requires=read('requirements.txt'),
    license=read('LICENSE'),
    long_description=read('README.md'),
    name=project_name,
    packages=find_packages(),
    platforms=['any'],
    scripts=[],
    test_suite='nose.collector',
    tests_require=read('requirements-dev.txt'),
    url='http://pypi/packages/' + project_name,
    version=__version__,
    cmdclass={},
    zip_safe=True
)
