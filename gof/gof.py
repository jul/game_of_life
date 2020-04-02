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
    """transpose a pattern at position X,Y in a matrix object with value ALIVE 
    by default to draw a single point at coordonates x=2, y=3 use 
    >>> at(grid 2,3 , pixel)

    """
    for dx,dy in pattern:
        grid.set(x+dx,y+dy,value)

def dirty(grid, times=1, all_pattern=all_pattern):
    """add random patterns n times at random position in a matrix object"""


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
    Cheat code : if speed is "unseeable" then the grid evolve without printing
    """

    if not hasattr(grid,'time'):
        grid.time=0
    time = grid.time

    n_grid = grid.duplicate()
    while times:
        times-=1
        time+=1
        if 'unseeable' != speed:
            os.system('clear')
            print(grid)
            print( "time:<%3d>" % time)
            sleep(1.0/speed)

        for x in range(grid.size_x):
            for y in range(grid.size_y):
                n_grid.set(x, y, grid.compute_state(x,y))
        n_grid.copy_in(grid)

    grid.time=time



def bleach(grid, x,y,empty_matrix=None):
    """time to bleach the grid and remove all leaving cells for a new start!
    The thrid parameter is an easter eggs to use any matrix object backend
    try  : 
    >>> from collections import defaultdict
    >>> bleach(grid, 10,10, defaultdict(bool, {}))
    
    to change the default implementation based on a boring array to a 
    defaultdict. 
    or 
    
    >>> from gof.weird_array import Bitmap
    >>> bleach(grid, 10,10, 1<<(10*10))
    

    """
    if not empty_matrix:
        empty_matrix=x*y*[DEAD]
    grid.__init__(x,y, empty_matrix)
    grid.time=0

