#!/usr/bin/python
from util.matrix import matrix
import os
from time import sleep

X = 12
Y = 18
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
#grid = matrix(X, Y, [0]* X*Y)
#from collections import defaultdict
#grid = matrix(X,Y,defaultdict(int,{}))
grid = matrix(X,Y,Bitmap(1<<(X*Y)))
#### end of golf

oscillator = [(0,0),(0,1),(0,2)]
stillator = [(0,0),(0,1),(1,0),(1,1)]
gliderator = [(0,2),(1,2),(2,2),(2,1),(0,0)]

def transpose(grid,x,y, pattern):
    for dx,dy in pattern:
        grid.set(x+dx,y+dy,ALIVE)

transpose(grid, 1,8, gliderator)
transpose(grid, 2,3, oscillator)
transpose(grid, 7,7, stillator)

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
