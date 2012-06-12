#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice, randint
import os
from time import sleep
oscillator = [(0,0),(0,1),(0,2)]
still = [(0,0),(0,1),(1,0),(1,1)]
glider = [(0,2),(1,2),(2,2),(2,1),(0,0)]
pixel = [(0,0)]

DEAD=0
ALIVE=1

all_pattern = [ oscillator, still, glider ]

##### helpers

def at(grid,x,y, pattern, value=ALIVE):
    """transpose a pattern at posution X,Y with value ALIVE by default
    to draw a single point at coordonates x=2, y=3 use 
    >>> at( 2,3 , pixel)

    """
    for dx,dy in pattern:
        grid.set(x+dx,y+dy,value)

def dirty(grid, times=1, all_pattern=all_pattern):
    """add random patterns at random position in the grid"""

    while times:
        times-=1
        at( grid, 
            randint(0, grid.size_x) ,
            randint(0,grid.size_y),
            choice(all_pattern)
        )

def evolve(grid,times=1, speed=1.0):
    """make grid evolve for times turn. Print all the grids if on linux 
    at speed times the default. 
    If show is False, nothing is printed, but the rules of games of life 
    are applied x times"""

    if not hasattr(grid,'time'):
        grid.time=0
    time = grid.time
    
    n_grid = grid.duplicate()
    while times:
        times-=1
        time+=1
        if 'unseeable' != speed:
            os.system('clear')
            print grid
            print "time:<%3d>" % time
            sleep(1.0/speed)
        
        for x in range(grid.size_x):
            for y in range(grid.size_y):
                if grid.get(x, y):
                    n_grid.set(x, y, grid.nb_living_around(x, y) in [2, 3])
                else:
                    n_grid.set(x, y, grid.nb_living_around(x, y) == 3)
        n_grid.copy_in(grid)


    grid.time=time
    


def bleach(grid, x,y,empty_matrix=None):
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
    grid.__init__(x,y, empty_matrix and empty_matrix or x*y*[DEAD])
    grid.time=0


