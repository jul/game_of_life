#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Game of Life console. 
small play ground for leanning python, or just having fun.

To use the console with an empty grid: 
    python -i -mgof.console
or
    bpython -i -mgof.console

To use the console with a pseudo animation: 
    python -i -mgof.demo

Avalailble variable : 
* grid your playground a matrix of cellular automata
* patterns : pixel, still, oscillator, glider
    they are singular patterns to play with in game of life.
* all_pattern : a list of all patterns (except pixel)
* matrix : the class name of grid is imported for educationnal purpose
* DEAD, ALIVE

Available functions:
* intro() : a short summary of all available functions
* bleach(...) a function to init the grid
* at(...) a function to draw a pattern on the grid
* rand_pattern() : a function to add random pattern in your grid
* evolve(...) make the game evolve for some time. If your terminal and/or 
	interactive python supports it, it will make a continuous animation

* use help(function_name) to know more  yes it is a builtin ^_^

"""
from .matrix import matrix
from time import sleep
from .gof import glider, oscillator, still, pixel, all_pattern
from .gof import evolve, bleach,dirty, DEAD, ALIVE, at
#### Constants and globals
__all__ = [ 
    "matrix","at",
    "grid", "intro", 
    "glider", "oscillator", "still","pixel","all_pattern",
    "evolve", "bleach", "dirty", "DEAD", "ALIVE" ]

x=10
y=30
def intro():
    print(__doc__)
    print("""
    you are left with an empty grid of %dx%d to play with, have fun""" % (x,y))

grid=matrix(x,y,x*y*[DEAD])



if '__main__' == __name__:
    print(__doc__)

