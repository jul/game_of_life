#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Game of Life console. small play ground for leanning python, or just having fun.

To us the console : 
    python -mgof.console or bpython -mgof.console 

Avalailble globals : 
* X, Y the size of the grid
* bleach(...) a function to init the grid
* grid your *empty* grid where game of life will evolve. print grid to sse it
* time : current iteration
* speed : speed for pseudo animation
* schmutzig : a list of pre-stored regular pattern
* at(...) a function to draw a pattern on the grid
* rand_pattern() : a function to add random pattern in your grid
* play(...) make the game evolve for some time. If your terminal and/or 
	interactive python supports it, it will make a continuous animation

* use help(function_name) to know more  yes it is a builtin ^^

"""
from matrix import matrix
from time import sleep
from .gof import glider, oscillator, still, pixel, all_pattern
from .gof import evolve, bleach,dirty, DEAD, ALIVE
#### Constants and globals
__all__ = [ 
    "matrix",
    "playground", "sleep","intro", 
    "glider", "oscillator", "still","pixel","all_pattern",
    "evolve", "bleach", "dirty", "DEAD", "ALIVE" ]

x=10
y=30
grid=matrix(x,y,x*y*[DEAD])
sleep=1.0
def intro(): print __doc__



if '__main__' == __name__:
    print __doc__
