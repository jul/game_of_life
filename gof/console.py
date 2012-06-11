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

from .matrix import matrix
import os
from time import sleep
from random import randint

#### Constants and globals
X = 22
Y = 60
DEAD = 0
ALIVE = 1
grid=None
time=0
speed=1.0
#### INIT



oscillator = [(0,0),(0,1),(0,2)]
still = [(0,0),(0,1),(1,0),(1,1)]
glider = [(0,2),(1,2),(2,2),(2,1),(0,0)]
pixel = [(0,0)]

all_pattern = [ oscillator, still, glider ]

##### helpers

def at(x,y, pattern, value=ALIVE):
    """transpose a pattern at posution X,Y with value ALIVE by default
    to draw a single point at coordonates x=2, y=3 use 
    >>> at( 2,3 , pixel)

    """
    global grid
    for dx,dy in pattern:
        grid.set(x+dx,y+dy,value)

def schmutzig(times=1):
    """add random patterns at random position in the grid"""

    global grid
    global all_pattern
    while times:
        times-=1
        at( randint(0, grid.size_x),randint(0,grid.size_y),all_pattern[
            randint(0,len(all_pattern)-1)
        ])

def play(times=1, show=True):
    """make grid evolve for times turn. Print all the grids if on linux 
    at speed times the default. 
    If show is False, nothing is printed, but the rules of games of life 
    are applied x times"""

    global grid
    global time
    global speed
    while times:
        if show:
            os.system('clear')
        times-=1
        time+=1
        if show:
            print grid
            print "time:<%3d>" % time
            sleep(1.0/speed)
        n_grid = grid.copy()
        for x in range(grid.size_x):
            for y in range(grid.size_y):
                if grid.get(x, y):
                    n_grid.set(x, y, grid.nb_living_around(x, y) in [2, 3])
                else:
                    n_grid.set(x, y, grid.nb_living_around(x, y) == 3)
        grid = n_grid

def bleach(x=X,y=Y, _with=None):
    """time to bleach the grid and remove all leaving cells for a new start!
    The thrid parameter is an easter eggs to use any array of mutable.
    try  : 
    >>> from collections import defaultdict
    >>> bleach(10,10, defaultdict(bool, {}))
    
    to change the default implementation based on a boring array to a 
    defaultdict. 
    or 
    
    >>> from gof.weird_array import Bitmap
    >>> bleach(10,10, 1<<(10*10))
    
    To store your states in an int. 
    
    if you do use this option, remember you *MUST* sepcify it 
    every time you use bleach.
    """


    
    global grid
    global time
    global X,Y
    X=x
    Y=y
    time = 0
    grid = matrix(x, y, _with if _with else [DEAD]*x*y)

### now let's play
bleach(X, Y)

def intro(): print __doc__

if '__main__' == __name__:
    print __doc__
