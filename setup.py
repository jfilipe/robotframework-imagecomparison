#!/usr/bin/env python

from distutils.core import setup

VERSION = '0.1'

DESCRIPTION = """
ImageComparisonLibrary is a CSS testing library for Robot Framework.
"""[1:-1]


CLASSIFIERS = """
Development Status :: 4 - Beta
License :: Public Domain
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(name         = 'robotframework-imagecomparison',
      version      = VERSION,
      description  = 'CSS testing library for Robot Framework',
      long_description = DESCRIPTION,
      author       = 'Jason Filipe',
      author_email = 'jason.filipe@gmail.com',
      url          = 'https://github.com/jfilipe/robotframework-imagecomparison',
      license      = 'Public Domain',
      keywords     = 'robotframework testing css styles styling frontend automation',
      platforms    = 'any',
      classifiers  = CLASSIFIERS.splitlines(),
      package_dir  = {'': 'src'},
      packages     = ['ImageComparisonLibrary'],
      package_data = {'ImageComparisonLibrary': ['tests/*.txt']}
      )
