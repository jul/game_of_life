.. gof documentation master file, created by
   sphinx-quickstart on Mon Jun 11 14:10:28 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

* source : https://github.com/jul/game_of_life/
* ticketting : https://github.com/jul/game_of_life/issues
* docs : http://gof.readthedocs.org

Foreword: Dont Do This at Home ! 
================================

.. warning::
    Please don't

    * from module import *
    * if you do so (which is bad) don't forget to define __all__
   
   I guess I have no excuse others than lazyness. But I find it so easier to use.


Pathetic excuse #1
******************

I am doing a conway game of life's `Domain Specific Language`_, and this is the easiest 
way to do it. 

    .. _`Domain Specific Language`: http://en.wikipedia.org/wiki/Domain-specific_language

Pathetic excuse #2
******************

Pretty easy to use and code :) 

Pathetic excuse #3
******************

I am a rebel.


Game of life is a serious game
==============================

Contents:

.. toctree::
   quickstart
   install
   primitive
   :maxdepth: 2

Changelog
=========

v0.1.0
    * usable console
    * pypi package, because it make doc shorter.

v0.1.1
   * spotted a bug in reset (TOFIX)
   * default backend is hint
   * changed the code so that conway rules are only a turing machine encoded as an int
   * added the grid.mutate(nb_flip=n) that flip randomly nbits in the conway code

v 0.1.2
   * Added another demo demo2 to show the result of flipping n bit on a cellular automata

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

