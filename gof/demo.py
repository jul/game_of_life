#!/usr/bin/python
import os
from .console import *
x,y=16,14
speed=5
### All these works ! 
#grid = matrix(x, y, bytearray(x*y))
#from numpy import array,zeros
#grid = matrix(x, y, zeros(x*y))
#grid = matrix(x, y, [DEAD]* x*y)
#from collections import defaultdict
#grid = matrix(x,y,defaultdict(int,{}))
from .weird_array import Bitmap, SparseArray
grid = matrix(x,y,Bitmap(ALIVE<<x*y))
#grid = matrix(x,y,SparseArray(set()))

at(grid, 3,9, glider)
at(grid, 2,2, oscillator)
at(grid, 6,5, still)

def reset(grid=grid):
    grid.__init__(x,y,Bitmap(ALIVE<<x*y))

evolve(grid, 160,speed)

