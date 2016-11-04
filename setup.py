#!/usr/bin/env python3

# distutils have no entry_points, fail if setuptools are not available
from setuptools import setup
import os
import dwmash

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Full list of classifiers can be found here:
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLS = \
 [ 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
 , 'Development Status :: 3 - Alpha'
 , 'Environment :: Web Environment'
 , 'Intended Audience :: System Administrators'
 , 'Operating System :: Unix'
 , 'Programming Language :: Python'
 , 'Topic :: Database :: Database Engines/Servers'
 ]

REQS = [
      'sqlalchemy >= 1.1.0'
    , 'pytz >= 2016.1'
    ]

CONSOLE_SCRIPTS = [
      'dwmash=dwmash.entry:dwmash'
    , 'dwmash-util=dwmash.entry:dwmash_util'
    ]

setup(
      name             = dwmash.pkgname
    , description      = dwmash.__description__
    , version          = dwmash.__version__
    , author           = dwmash.__author__
    , author_email     = dwmash.__author_email__
    , license          = dwmash.__license__
    , url              = dwmash.__url__
    , long_description = read('README')
    , packages         = [ 'dwmash' ]
    , classifiers      = CLS
    , install_requires = REQS
    , entry_points     = {
          'console_scripts' : CONSOLE_SCRIPTS
        }
    )

