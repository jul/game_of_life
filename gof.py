#!/usr/bin/python
from gof.matrix import matrix
import os
from time import sleep

X = 16
Y = 14
DEAD = 0
ALIVE = 1

### All these works ! 
#grid = matrix(X, Y, bytearray(X*Y))
#from numpy import array,zeros
#grid = matrix(X, Y, zeros(X*Y))
#grid = matrix(X, Y, [DEAD]* X*Y)
#from collections import defaultdict
#grid = matrix(X,Y,defaultdict(int,{}))
from gof.weird_array import Bitmap, SparseArray
grid = matrix(X,Y,Bitmap(DEAD))
#grid = matrix(X,Y,SparseArray(set()))
#### end of golf

oscillator = [(0,0),(0,1),(0,2)]
still = [(0,0),(0,1),(1,0),(1,1)]
glider = [(0,2),(1,2),(2,2),(2,1),(0,0)]

def at(grid,x,y, pattern):
    for dx,dy in pattern:
        grid.set(x+dx,y+dy,ALIVE)

at(grid, 1,8, glider)
at(grid, 2,3, oscillator)
at(grid, 6,5, still)

time=0
while True:
    time+=1
    os.system('clear')
    print grid
    print 'time is <%03d>' % time
    sleep(1)
    n_grid = grid.copy()
    for x in range(X):
        for y in range(Y):
            if grid.get(x, y):
                n_grid.set(x, y, grid.nb_living_around(x, y) in [2, 3])
            else:
                n_grid.set(x, y, grid.nb_living_around(x, y) == 3)
    grid = n_grid
