#!/usr/bin/python
from gof.matrix import matrix
from gof.gof import evolve, DEAD,ALIVE, at, all_pattern, glider, oscillator
from gof.gof import still, pixel,bleach,dirty
import os
from time import sleep
x,y=16,14

### All these works ! 
#grid = matrix(x, y, bytearray(x*y))
#from numpy import array,zeros
#grid = matrix(x, y, zeros(x*y))
grid = matrix(x, y, [DEAD]* x*y)
#from collections import defaultdict
#grid = matrix(x,y,defaultdict(int,{}))
from gof.weird_array import Bitmap, SparseArray
#grid = matrix(x,y,Bitmap(ALIVE<<x*y))
#grid = matrix(x,y,SparseArray(set()))

at(grid, 3,9, glider)
at(grid, 2,2, oscillator)
at(grid, 6,5, still)

def reset(grid=grid):
    grid.__init__(x,y,Bitmap(ALIVE<<x*y))

evolve(grid, 100,5)

