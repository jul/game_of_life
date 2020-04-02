#!/usr/bin/env pyrhon
# -*- coding: "utf-8" -*-

from distutils.command.build_py import build_py as _build_py
from distutils.core import setup

def test():
    """Specialized Python source builder."""
setup(
        name='gof',
        version='0.1.3',
        author='Julien Tayon',
        author_email='julien@tayon.net',
        packages=['gof'],
        url='http://gof.readthedocs.org/',
        license='LICENSE.txt',
        description='''a little fun with Conway's Game Of Life''',
        requires=[ ],
        classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Python Software Foundation License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
)
