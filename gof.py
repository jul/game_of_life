#!/usr/bin/python
from util.matrix import matrix
import os
from time import sleep

X = 12
Y = 18
DEAD = 0
ALIVE = 1

#grid = matrix(X, Y, bytearray(X*Y))
#from numpy import array,zeros
#grid = matrix(X, Y, zeros(X*Y))

grid = matrix(X, Y, [0]* X*Y)

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
