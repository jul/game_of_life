#!/usr/bin/python
from util.matrix import matrix
import os
from time import sleep

X = 16
Y = 14
DEAD = 0
ALIVE = 1

class Bitmap(object):
    def __init__(self,_int):
        self._int = int(_int)

    def __setitem__(self,offset, val):
        if val:
            self._int |= 1<<offset
        else:
            self._int &= ~(1<<offset)

    def __getitem__(self,offset):
        return int(bool(self._int & 1<<offset))

    def copy(self):
        return Bitmap(self._int)



### All these works ! 
#grid = matrix(X, Y, bytearray(X*Y))
#from numpy import array,zeros
#grid = matrix(X, Y, zeros(X*Y))
#grid = matrix(X, Y, [DEAD]* X*Y)
#from collections import defaultdict
#grid = matrix(X,Y,defaultdict(int,{}))
grid = matrix(X,Y,Bitmap(DEAD))
#### end of golf

oscillator = [(0,0),(0,1),(0,2)]
still = [(0,0),(0,1),(1,0),(1,1)]
glider = [(0,2),(1,2),(2,2),(2,1),(0,0)]

def transpose(grid,x,y, pattern):
    for dx,dy in pattern:
        grid.set(x+dx,y+dy,ALIVE)

transpose(grid, 1,8, glider)
transpose(grid, 2,3, oscillator)
transpose(grid, 6,5, still)

time=0
os.system('clear')
while True:
    time+=1
    os.system('clear')
    print grid
    print 'time is <%4d>' % time
    sleep(1)
    n_grid = grid.copy()
    for x in range(X):
        for y in range(Y):
            if grid.get(x, y):
                n_grid.set(x, y, grid.nb_living_around(x, y) in [2, 3])
            else:
                n_grid.set(x, y, grid.nb_living_around(x, y) == 3)
    grid = n_grid
